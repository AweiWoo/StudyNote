#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

#自己试一下一些标准库中的itertools.chain函数

def chain(*iterables):  #iterables是生成器或可迭代对象
    for it in iterables:
        for i in it:  #使用两个for循环产出所有可迭代对象的值
            yield i

#使用yeild from改进
def chain2(*iterables):
    for i in iterables:
        yield from i    #yield from i 完全代替了内层的 for 循环

s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))  #['A', 'B', 'C', 0, 1, 2]
print(list(chain2(s, t))) #['A', 'B', 'C', 0, 1, 2]

