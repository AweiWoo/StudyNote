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
        #已经不是生成器函数了，没有yeild关键字了，而是使用了生成器表达式
        return (match.group() for match in RE_WORD.finditer(self.text))