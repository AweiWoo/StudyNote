#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

"""
激活和关闭 demo_exc_handling, 没有异常
>>> from coro_exec_demo import demo_exc_handling
>>> exc_coro = demo_exc_handling()
>>> next(exc_coro)
-> coroutine started
>>> exc_coro.send(11)
-> coroutine received: 11
>>> exc_coro.send(22) 
-> coroutine received: 22
>>> exc_coro.close() 
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(exc_coro)
'GEN_CLOSED'

把DemoException异常传入demo_exc_handling协程，他会处理，然后继续
>>> from coro_exec_demo import demo_exc_handling, DemoException
>>> exc_coro = demo_exc_handling()
>>> next(exc_coro)    
-> coroutine started
>>> exc_coro.send(11)
-> coroutine received: 11
>>> exc_coro.throw(DemoException)
*** DemoException handled. Continuing...
>>> getgeneratorstate(exc_coro) 
'GEN_SUSPENDED'
>>> exc_coro.send(22) 
-> coroutine received: 22
>>>
"""

class DemoException(Exception):
    """定义的异常类型"""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException: #特别处理 DemoException 异常。
            print('*** DemoException handled. Continuing...')
        else: #如果没有异常，那么显示接收到的值。
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.') #这一行永远不会执行。
        