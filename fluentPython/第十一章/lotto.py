#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import random
from tombola import Tombola

class LotteryBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)  #把参数构建为列表，创建副本而不是引用。

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)   #从self._balls中随机取出元素

    #重写基类方法，避免调用inspect方法，提升速度
    def loaded(self):            
        return bool(self._balls)   

    #重写基类方法，使用一行代码
    def inspect(self):
        return tuple(sorted(self._balls))