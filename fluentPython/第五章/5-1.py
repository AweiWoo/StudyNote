#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import random
class BingoCage:
    def __init__(self,items):
        self._items = list(items)
        #shuffle方法：将序列中的所有元素随机排列
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")
        
    def __call__(self):
        return self.pick()

bingo = BingoCage(range(4))
#可以通过对象的pick方法调用函数
print(bingo.pick())
print(bingo.pick())
#因为实现了__call__,所以可以直接使用对象加()的方法调用pick对象
print(bingo())
print(bingo())
print(bingo())