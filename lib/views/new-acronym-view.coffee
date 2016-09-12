{CompositeDisposable} = require 'atom'
{$, View, TextEditorView} = require "atom-space-pen-views"
path = require "path"
fs = require "fs-plus"

config = require "../config"
utils = require "../utils"
templateHelper = require "../helpers/template-helper"

module.exports =
class NewFileView extends View
  @fileType = "File" # override
  @pathConfig = "siteFilesDir" # override
  @fileNameConfig = "newFileFileName" # override

  @content: ->
    @div class: "acronyms-view", =>
      @label "Update Acronym", class: "icon icon-file-add"
      @div =>
        @label "Acronym", class: "message"
        @subview "acronym", new TextEditorView(mini: true)
        @label "Description", class: "message"
        @subview "description", new TextEditorView(mini: true)
        @label "Acronym File", class: "message"
        @subview "acronymFile", new TextEditorView(mini: true)
      @p class: "message", outlet: "message"
      @p class: "error", outlet: "error"

  initialize: ->
    utils.setTabIndex([@titleEditor, @pathEditor, @dateEditor])

    # save current date time as base
    @dateTime = templateHelper.getDateTime()

    @titleEditor.getModel().onDidChange => @updatePath()
    @pathEditor.getModel().onDidChange => @updatePath()
    # update pathEditor to reflect date changes, however this will overwrite user changes
    @dateEditor.getModel().onDidChange =>
      @pathEditor.setText(templateHelper.create(@constructor.pathConfig, @getDateTime()))

    @disposables = new CompositeDisposable()
    @disposables.add(atom.commands.add(
      @element, {
        "core:confirm": => @createFile()
        "core:cancel": => @detach()
      }))

  display: ->
    @panel ?= atom.workspace.addModalPanel(item: this, visible: false)
    @previouslyFocusedElement = $(document.activeElement)
    @dateEditor.setText(templateHelper.getFrontMatterDate(@dateTime))
    @pathEditor.setText(templateHelper.create(@constructor.pathConfig, @dateTime))
    @panel.show()
    @titleEditor.focus()

  detach: ->
    if @panel.isVisible()
      @panel.hide()
      @previouslyFocusedElement?.focus()
    super

  detached: ->
    @disposables?.dispose()
    @disposables = null

  createFile: ->
    try
      filePath = path.join(@getFileDir(), @getFilePath())

      if fs.existsSync(filePath)
        @error.text("File #{filePath} already exists!")
      else
        frontMatterText = templateHelper.create("frontMatter", @getFrontMatter(), @getDateTime())
        fs.writeFileSync(filePath, frontMatterText)
        atom.workspace.open(filePath)
        @detach()
    catch error
      @error.text("#{error.message}")
