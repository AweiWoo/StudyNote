#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import re
import reprlib 

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text     #不再需要 words 列表。

    def _repr(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def _iter__(self):
        #finditer 函数构建一个迭代器，包含 self.text 中匹配RE_WORD 的单词，产出 MatchObject 实例
        for match in RE_WORD.finditer(self.text):  
            yield match.group()  #match.group() 方法从 MatchObject 实例中提取匹配正则表达式的具体文本