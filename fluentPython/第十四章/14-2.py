#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end #None -->无穷数列

    def __iter__(self):
        #首项与其他项的类型一样，想到最好的方式是，先做加法运算，然后使用计算结果的类型强制转换生成的结果
        result = type(self.begin + self.step)(self.begin)
        forever =self.end is None  #提高可读性,如果 self.end 属性的值是 None，那么 forever 的值是 True
        index = 0 
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin +self.step * index


#如果创建一个类只是为了构建生成器而去实现__iter__ 方法，那还不如直接使用生成器函数。
def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0 
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index