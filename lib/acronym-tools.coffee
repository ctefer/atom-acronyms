{Range, Point, CompositeDisposable} = require 'atom'
path = require 'path'


regexPatternIn = (pattern, list) ->
  for item in list
    if pattern.test item
      return true
  return false


AtomAcronyms =
  config:
    smartBlockSelection:
      type: 'boolean'
      description: 'Do not select whitespace outside logical string blocks'
      default: true
    pythonPath:
      type: 'string'
      default: ''
      title: 'Path to python directory'
      description: '''
      Optional. Set it if default values are not working for you or you want to use specific
      python version. For example: `/usr/local/Cellar/python/2.7.3/bin` or `E:\\Python2.7`
      '''

  subscriptions: null

  _issueReportLink: "https://github.com/michaelaquilina/python-tools/issues/new"

  activate: (state) ->
    # Events subscribed to in atom's system can be easily cleaned up with a CompositeDisposable
    @subscriptions = new CompositeDisposable
    @subscriptions.add(
      atom.commands.add 'atom-text-editor',
      'atom-acronyms:update-definition': => @updatedefinition()
    )
    @subscriptions.add(
      atom.commands.add 'atom-text-editor',
      'atom-acronyms:print-acronyms': => @printacronyms()
    )
    @subscriptions.add(
      atom.commands.add 'atom-text-editor',
      'atom-acronyms:define-first': => @definefirst()
    )

    env = process.env
    pythonPath = atom.config.get('acronym-tools.pythonPath')
    path_env = null

    if /^win/.test process.platform
      paths = ['C:\\Python2.7',
               'C:\\Python27',
               'C:\\Python3.4',
               'C:\\Python34',
               'C:\\Python3.5',
               'C:\\Python35',
               'C:\\Program Files (x86)\\Python 2.7',
               'C:\\Program Files (x86)\\Python 3.4',
               'C:\\Program Files (x86)\\Python 3.5',
               'C:\\Program Files (x64)\\Python 2.7',
               'C:\\Program Files (x64)\\Python 3.4',
               'C:\\Program Files (x64)\\Python 3.5',
               'C:\\Program Files\\Python 2.7',
               'C:\\Program Files\\Python 3.4',
               'C:\\Program Files\\Python 3.5']
      path_env = (env.Path or '')
    else
      paths = ['/usr/local/bin', '/usr/bin', '/bin', '/usr/sbin', '/sbin']
      path_env = (env.PATH or '')

    path_env = path_env.split(path.delimiter)
    path_env.unshift pythonPath if pythonPath and pythonPath not in path_env
    for p in paths
      if p not in path_env
        path_env.push p
    env.PATH = path_env.join path.delimiter

    @provider = require('child_process').spawn(
      'python', [__dirname + '/tools.py'], env: env
    )

    @readline = require('readline').createInterface(
      input: @provider.stdout
      output: @provider.stdin
    )

    @provider.on 'error', (err) =>
      if err.code == 'ENOENT'
        atom.notifications.addWarning("""
          atom-acronyms was unable to find your machine's python executable.

          Please try set the path in package settings and then restart atom.

          If the issue persists please post an issue on
          #{@_issueReportLink}
          """, {
            detail: err,
            dismissable: true
          }
        )
      else
        atom.notifications.addError("""
          atom-acronyms unexpected error.

          Please consider posting an issue on
          #{@_issueReportLink}
          """, {
              detail: err,
              dismissable: true
            }
        )
    @provider.on 'exit', (code, signal) =>
      if signal != 'SIGTERM'
        atom.notifications.addError(
          """
          python-tools experienced an unexpected exit.

          Please consider posting an issue on
          #{@_issueReportLink}
          """, {
            detail: "exit with code #{code}, signal #{signal}",
            dismissable: true
          }
        )

  deactivate: ->
    @subscriptions.dispose()
    @provider.kill()
    @readline.close()

  updatedefinition: ->
  printacronyms: ->
  definefirst: ->
    editor = atom.workspace.getActiveTextEditor()
    grammar = editor.getGrammar()

    bufferPosition = editor.getCursorBufferPosition()

    payload =
      type: type
      path: editor.getPath()
      source: editor.getText()
      line: bufferPosition.row
      col: bufferPosition.column
      project_paths: atom.project.getPaths()

    # This is needed for the promise to work correctly
    handleJediToolsResponse = @handleJediToolsResponse
    readline = @readline

    return new Promise (resolve, reject) ->
      response = readline.question "#{JSON.stringify(payload)}\n", (response) ->
        handleJediToolsResponse(JSON.parse(response))
        resolve()


module.exports = PythonTools
