#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import itertools

from tombola import Tombola
from bingo import BingoCage

class AddableBingoCage(BingoCage):

    def __add__(self, other):
        
        if isinstance(other, Tombola):  #使用抽象基类判断,保证other是Tombola类型
            #　调用 AddableBingoCage 构造方法构建一个新实例，作为结果返回
            return AddableBingoCage(self.inspect() + other.inspect()) 
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = "right operand in += must be {!r} or an iterable"
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)
        return self  #把修改后的 self 作为结果返回。