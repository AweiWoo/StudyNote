#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from clockdeco_demo import clock 
import functools

@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n 
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    print(fibonacci(6))