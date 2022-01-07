#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

# 实现典型的迭代器设计模式

import re
import reprlib 

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def _repr(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):    #没有实现__getitem__方法，而是实现了__iter__，明确表明这个类可以迭代
        return SentenceIterator(self.words)    #根据可迭代协议，__iter__ 方法实例化并返回一个迭代器
 

class SentenceIterator:      #SentenceIterator是一个迭代器

    def __init__(self, words):
        self.words = words    #SentenceIterator 实例引用单词列表
        self.index = 0        #self.index 用于确定下一个要获取的单词

    def __next__(self):       #迭代器必须实现方法
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):    
        return self