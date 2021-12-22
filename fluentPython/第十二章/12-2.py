#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import collections

class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

dd = DoppelDict2(one=1)
print(dd)  #{'one': [1, 1]}
dd['two'] = 2
print(dd)   #{'one': [1, 1], 'two': [2, 2]}
dd.update(three=3)
print(dd)   #{'one': [1, 1], 'two': [2, 2], 'three': [3, 3]}


class AnswerDict2(collections.UserDict):
    def __getitem__(self, key):
        return 42

ad = AnswerDict2(a='foo', b='too')
print(ad['a'])  #42
d = {}
d.update(ad)
print(d)   #{'a': 42, 'b': 42}