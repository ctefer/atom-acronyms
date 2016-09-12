#!/usr/bin/env python

import os

from distutils.core import setup

modules = [
    'acronyms.tests',
]



setup(name='Acronyms',
      version='0.01',
      description='Acronyms Library',
      author='Chris Tefer',
      author_email='ctefer@gmail.com',
      url='https://ctefer.github.io/',
      packages=['acronyms'] + modules,
     )

