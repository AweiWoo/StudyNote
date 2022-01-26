#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

"""
调用send方法不会返回值
>> from coroaverage2 import average
>>> coro_avg = average()
>>> next(coro_avg) 
>>> coro_avg.send(10)
>>> coro_avg.send(30) 
>>> coro_avg.send(6.5) 
传入None，抛出StopIteration一次，异常对象的value值保存返回值
>>> coro_avg.send(None) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration: Result(count=3, average=15.5)

使用try语句捕获异常，获取average的返回值
>>> coro_avg = average()
>>> next(coro_avg)       
>>> coro_avg.send(10)    
>>> coro_avg.send(30)    
>>> coro_avg.send(6.5)   
>>> 
>>> try:
...     coro_avg.send(None)
... except StopIteration as exc:
...     result = exc.value
... 
>>> result
Result(count=3, average=15.5)
"""

from collections import namedtuple

Result = namedtuple('Result', 'count average')

def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield      #yield右边没有对象，不用产出值
        if term is None:
            break         #为了可以跳出循环，得到返回值，协程必须正常终止
        total += term
        count += 1
        average = total/count
    return Result(count, average)   #返回一个namedtuple，python3.3之前，生成器返回值解释器会报错