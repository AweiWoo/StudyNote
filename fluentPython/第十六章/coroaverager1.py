#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

"""
用于计算移动平均值的协程

>>> from coroaverager1 import average
>>> from inspect import getgeneratorstate
>>> coro_avg = average() 
>>> getgeneratorstate(coro_avg) 
'GEN_SUSPENDED'
>>> coro_avg.send(10)
10.0
>>> coro_avg.send(30) 
20.0
>>> coro_avg.send(5)  
15.0
>>>

"""

from coroutil import coroutine

@coroutine
def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count