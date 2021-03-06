#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import time
import functools

def clock(func):   
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args) 
        elasped =  time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%s' % (k, w) for k, w in sorted(kwargs.items)]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elasped,name, arg_str, result))
        return result
    return clocked 