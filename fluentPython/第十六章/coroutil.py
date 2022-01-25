#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from functools import wraps

def coroutine(func):
    @wraps(func)           #保留原函数的属性
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer