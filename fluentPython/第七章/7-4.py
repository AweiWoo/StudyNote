#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import time
from clockdeco_demo import clock 

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)
# factorial作为参数传给clock函数,clock函数返回clocked函数。python编译器在背后把clocked赋值给factorial
# factorial保存的clocked函数的引用。每次调用factorial(n)都是执行clocked(n)

if __name__ == '__main__':
    print('*' * 40 , 'Calling snooze(2)')
    snooze(2)
    print('*' * 40 ,'Calling factorial(6)')
    print('6! =', factorial(6))


