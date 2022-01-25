#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

#生成一个闭包，在多次调用之间跟踪 total 和 count 变量的值,何使用协程实现
def average():
    total = 0.0 
    count = 0
    average = None
    while True:
        #yeild用于暂停执行协程，把结果发给调用方；还用于接收调用方后面发给协程的值，恢复无限循环。
        term = yield average 
        total += term
        count += 1
        average = total/count

#这个无限循环表明，只要调用方不断把值发给这个协程，它就会一直接收值，然后生成结果。仅当调用方在协程上调用 .close() 方
#法，或者没有对协程的引用而被垃圾回收程序回收时，这个协程才会终止。

coro_avg = average()
next(coro_avg)
print(coro_avg.send(10))
print(coro_avg.send(20))