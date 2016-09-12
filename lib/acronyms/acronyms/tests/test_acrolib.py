#!/usr/bin/env python
"""
Test the acrolib functions

"""

import os, re
from acronyms import acrolib

acronym_easy = "DoD, U.S.A, UAF, ReGeX"

acronym_ipsum_lorem = \
"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ex eros, euismod sit amet imperdiet ac," + \
"mattis ut diam. Nam consequat turpis EGET mauris iaculis convallis id nec DuD. Nulla iaculis nisi enim," + \
"vel tristique ipsum porta gravida. Phasellus ultricies tellus ac volutpat aliquam. Morbi eget erat in" + \
"nisl feugiat consectetur ac NEC dui. Etiam condimentum dolor vel lobortis volutpat. Nunc eu dignissim" + \
"erat. Quisque consequat dui at orci venenatis, sed consequat urna volutpat. DuD in nunc aliquet, aliquet" + \
"dui et, rhoncus sem. Sed rhoncus pharetra tristique." + \
"\n" + \
"Phasellus et fringilla turpis, a tincidunt leo. Aliquam ut tincidunt est, interdum VIT rhoncus mauris. Etiam" + \
"sagittis PoRt sem, vitae mattis mauris. Integer in luctus ante. PRO luctus nisi in elit tincidunt" + \
"placerat. Donec et sollicitudin tellus. Nunc tempor ligula quis elit pretium, in consequat tellus tempor." + \
"\n" + \
"CRA placerat lacinia massa in placerat. Maecenas maximus laoreet ipsum sed viverra. Donec suscipit" + \
"tincidunt enim a pharetra. In ac semper turpis. Morbi id porta lacus. Maecenas elit dui, tempus nec" + \
"tristique id, malesuada sed leo. Nam suscipit, elit in elementum ullamcorper, lectus nisi sodales tellus," + \
"sed dignissim risus mauris eget massa. Vestibulum faucibus, arcu a laoreet mollis, libero erat ultricies" + \
"magna, sed tempus lorem augue sit amet ex. Donec pellentesque bibendum enim, ac gravida est euismod eget." + \
"Aliquam ullamcorper tincidunt diam. Nulla ut accumsan urna." + \
"\n" + \
"Vivamus efficitur velit non ullamcorper rhoncus. Maecenas vestibulum neque in erat accumsan, eget fringilla" + \
"risus ullamcorper. Duis at massa nisi. Etiam justo mauris, accumsan et lectus sed, aliquam euismod arcu." + \
"Curabitur vel sapien lobortis lectus congue sollicitudin eget nec lectus. CRA turpis leo, gravida in" + \
"pharetra ut, mattis eu neque. Sed non odio id libero vestibulum PoRt vehicula sit amet vel dui. Sed blandit" + \
"mi ac eleifend sagittis. Integer VIT iaculis tellus. Integer massa lorem, dignissim eu convallis eu," + \
"blandit a leo. In finibus, felis VIT tempus lacinia, velit erat pretium odio, in ullamcorper velit mi eu felis." + \
"\n" + \
"Nulla gravida nibh sed mattis viverra. Donec interdum metus at tempor dignissim. Sed arcu diam, blandit" + \
"sit amet leo eu, venenatis cursus sem. Sed eget imperdiet lacus, vitae efficitur justo. Nunc in est" + \
"ultrices, rutrum felis sit amet, ultricies arcu. Vivamus NEC massa euismod, molestie odio sed, vulputate" + \
"sem. Vivamus eu metus ornare, aliquet elit in, pharetra nunc. Curabitur ornare id arcu in sagittis."


def test_find():
    assert set(acrolib.find(acronym_easy)) == \
           set(['DoD', 'U.S.A', 'UAF', 'ReGeX'])
    assert set(acrolib.find(acronym_ipsum_lorem)) == \
           set(['DuD', 'PRO', 'EGET', 'DuD', 'NEC', 'CRA', 'VIT'])
def test_define_first():
    defins = {
        'DoD' : 'Deparment of Defense',
        'U.S.A.' : 'United States of America',
        'PRO' : 'Proctem Rebuso Ophella',
        'NEC' : 'Nam Eseaium Curabitur',
        'DuD' : 'Duadnum ulinite Dictatum',
    }

    assert acrolib.define_first(acronym_easy,\
                                'DoD', 'Department of Defense')== \
           'Department of Defense(DoD), U.S.A, UAF, ReGeX'
    a = acrolib.define_first_all(defins, acronym_ipsum_lorem)
    assert a.find('Proctem Rebuso Ophella(PRO)')
    assert a.find('Nam Eseaium Curabitur(NEC)')
    assert a.find('Duadnum ulinite Dictatum(DuD)')
