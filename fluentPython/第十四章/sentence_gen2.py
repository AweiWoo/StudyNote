#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import re
import reprlib 

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text

    def _repr(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def _iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()