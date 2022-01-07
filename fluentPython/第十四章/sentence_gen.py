#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import re
import reprlib 

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def _repr(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def _iter__(self):
        for word in self.words:
            yield word           #产出当前的 word
        return     #这个 return 语句不是必要的