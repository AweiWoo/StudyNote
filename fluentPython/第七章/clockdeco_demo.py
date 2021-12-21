#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import time

def clock(func):   #func是自由变量
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)  # 执行被装饰的函数
        elasped =  time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elasped,name, arg_str, result))
        return result
    return clocked #返回内部函数，取代被装饰的函数
