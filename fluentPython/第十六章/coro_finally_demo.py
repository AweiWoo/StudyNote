#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

"""
>>> from coro_finally_demo import DemoException, demo_finally 
>>> coro_avg = demo_finally()
>>> next(coro_avg) 
-> coroutine started
>>> coro_avg.send(11)
-> coroutine received: 11
>>> coro_avg.send(12) 
-> coroutine received: 12
>>> coro_avg.send(DemoException) 
-> coroutine received: <class 'coro_finally_demo.DemoException'>
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(coro_avg) 
'GEN_SUSPENDED'
>>> coro_avg.throw(DemoException) 
*** DemoException handled. Continuing...
>>> getgeneratorstate(coro_avg)   
'GEN_SUSPENDED'
>>> coro_avg.close()  
-> coroutine ending
>>>
"""

class DemoException(Exception):
    """定义的异常类型"""

def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')
