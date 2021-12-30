#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu
# 把句子划分为单词序列

import re
import reprlib

RE_WORD = re.compile('\w+')  #匹配字母、数字、下划线。等价于 [A-Za-z0-9_]

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text) #返回一个字符串列表，元素是正则表达式匹配的全部匹配

    def __getitem__(self, index):   #实现了此方法，对象就变得可迭代了
        return self.words[index]

    def __len__(self):      #完善序列类型，实现此方法
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    for word in s:
        print(word)    #实例时可以迭代的
    print(list(s))
    print(s[2])