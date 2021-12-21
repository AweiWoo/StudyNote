#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from tombola import Tombola
import random

class BingoCage(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()  #生成一种适合加密的随机字节序列
        self._items = [] 
        self.load(items)  #items的内容委托给load实现
    
    def load(self, items):  #实现基类中的抽象方法
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):    #实现基类中的抽象方法
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingCage')
        
    def __call__(self):  #让对象可调用，可以()
        self.pick()