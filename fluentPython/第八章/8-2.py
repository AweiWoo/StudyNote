#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

print(t1 == t2)
print(id(t1[-1]))
t1[-1].append(99)
#使用append,expand不会报错，但是用“+=”会报错
#t1[-1]+=[99]

print(t1)
print(id(t1[-1]))
print(t1 == t2)