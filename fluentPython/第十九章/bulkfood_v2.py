#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

class LineItem:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property  #装饰读值方法
    def weight(self): # 实现特性的方法，其名称都与公开属性的名称一样——weight
        return self.__weight #真正的值存储在私有属性 __weight 中

    @weight.setter #这个装饰器把读值方法和设值方法绑定在一起
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')