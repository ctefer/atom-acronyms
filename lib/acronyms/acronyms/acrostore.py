#!/usr/bin/env python
"""
Provides functions for storing, retrieving, and printing information.

load(file) - retrieve json data for the acronyms from file
dump(acronym dictionary, file) - update or create an acronym file
md_table(acronym dictionary) - returns the acronym dictionary
    as a markdown table
"""

import json
import os.path

DEFAULT_JSON = 'acronyms.json'
_dir_setup = os.path.dirname(os.path.realpath(__file__))

def load(acr_file=DEFAULT_JSON):

    data = {}

    try:
        data = _read_json(acr_file)
    except:
        print('File does not exist or is not an acronym dictionary file\n')
        raise

    return data

def dump(acroset, save=DEFAULT_JSON):

    data = {}

    try:
        data = load(save)
    except:
        print('Creating acronym file:',_acronym_json)

    data.update(acroset)

    with open(save, 'w') as json_file:
        json.dump(data,json_file)
        json_file.close()

    return data

def md_table(acroset, title='Acronym', defin='Definition'):

    data_str = ''

    data_str = _mline(title,defin)
    data_str += _mline('---','---')
    for k,v in acroset.items():
        data_str += _mline(str(k),str(v))

    return data_str

def html_table(acroset, title='Acronym', defin='Definition'):

    data_str = ''

    data_str = '<table>\n'
    data_str += _hrow(title, defin)
    for k,v in acroset.items():
        data_str += _hrow(str(k),str(v))
    data_str += '</table>\n'

    return data_str

def _read_json(acr_file):

    j_data = {}

    try:
        with open(acr_file, 'r') as json_file:
            j_data = json.load(json_file)
            json_file.close()
    except:
        raise

    return j_data

def _hrow(*args):
    return _print_line('<tr><td>', '</td><td>', '</td></tr>\n', args)

def _mline(*args):
    return _print_line('|', '|', '|\n', args)

def _print_line(start, sepr, end, *args):
    line = start
    for k,v in args:
        line += k + sepr + v
    line += end
    return line
