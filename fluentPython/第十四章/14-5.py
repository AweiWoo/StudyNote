#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import random

def d6():
    return random.randint(1, 6)  

#通过d6函数，随机产生数字，当产生为1的时候停止
d6_iter = iter(d6, 1) 
print(d6_iter)    #<callable_iterator object at 0x00000238D922A730>
for roll in d6_iter:
    print(roll)