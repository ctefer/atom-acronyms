# Introduction

## Architecture

## API
* `setup.py` - Initial setup module
* `check_acronym( text )` - Checks the text provided and returns true if the text is a possible acronym.
* `store_acronym( acr, desc)` - Stores the acronym to the current list.
* `get_description( acr )` - Retrieves the description of the provided acronym.
* `get_acronym( desc )` - Retrieves the acronym of the provided description.
* `serialize_acronyms` - All stored acronyms are serialized and returned.
* `pretty_print` - Prints the acronyms in a table.
