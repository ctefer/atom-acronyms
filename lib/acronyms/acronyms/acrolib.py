#!/usr/bin/env python
"""
Provides functions used to manipulate and find acronyms

Doesn't handle cases where the Acronym contains periods at the end of a
sentence. Such as sentence ending with U.S.A. This will have to be corrected.

"""
import re

acronym_finds = [ r'\b(?:[A-Z](?:\.|[aeiou]*)){2,}(?:\.|\b)']

def find(text):
    _list = list()

    for reg in acronym_finds:
        c = re.compile(reg)
        matches = c.findall(text)
        if matches is not None:
            for m in matches:
                m = _remove_dot(m)
                _list.append(m)

    # remove duplicates
    return(list(set(_list)))

def define_first(text, acro, desc):
    return re.sub(acro, desc + '(' + acro + ')', text, 1)

def define_first_all(acros, text):
    for a in acros:
        text = define_first(text, a, acros[a])

    return text

def _remove_dot(acro):
    ind = len(acro) - 1
    if ind == acro.find('.'):
        acro = acro.split('.')[0]
    return acro
