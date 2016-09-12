#!/usr/bin/env python
"""
Test the acrostore functions

"""

import os
from acronyms import acrostore

acronym_load = {
    'USA'   : 'United States of America',
    'TBD'   : 'To Be Determined',
    'DoD'   : 'Department of Defense',
    'HTML'  : 'Hypertext Markup Language',
    'FOUO'  : 'For Official Use Only',
    'ReGeX' : 'Regular Expression',
    'OS'    : 'Operating System',
}

def test_acroset_dumpload():
    test_file = 'data.json'
    assert acrostore.dump({}, test_file) == {}
    assert acrostore.dump(acronym_load, test_file) == acronym_load
    assert acrostore.load(test_file) == acronym_load

    dump_test = {
        'OS' : 'Open Source',
    }

    acronyms_update = acrostore.load(test_file)
    acronyms_update.update(dump_test)

    assert acrostore.dump(dump_test, test_file) == acronyms_update
    

    os.remove(test_file)
    print('Test file has been removed')

def test_acroset_print():

    assert acrostore.md_table(acronym_load) == \
        '|Acronym|Definition|\n' + \
        '|---|---|\n' + \
        '|ReGeX|Regular Expression|\n' + \
        '|USA|United States of America|\n' + \
        '|FOUO|For Official Use Only|\n' + \
        '|DoD|Department of Defense|\n' + \
        '|HTML|Hypertext Markup Language|\n' + \
        '|OS|Operating System|\n|TBD|To Be Determined|\n'
    assert acrostore.html_table(acronym_load, 'Test', 'Desc') == \
        '<table>\n' + \
        '<tr><td>Test</td><td>Desc</td></tr>\n' + \
        '<tr><td>ReGeX</td><td>Regular Expression</td></tr>\n' + \
        '<tr><td>USA</td><td>United States of America</td></tr>\n' + \
        '<tr><td>FOUO</td><td>For Official Use Only</td></tr>\n' + \
        '<tr><td>DoD</td><td>Department of Defense</td></tr>\n' + \
        '<tr><td>HTML</td><td>Hypertext Markup Language</td></tr>\n' + \
        '<tr><td>OS</td><td>Operating System</td></tr>\n' + \
        '<tr><td>TBD</td><td>To Be Determined</td></tr>\n' + \
        '</table>\n'
