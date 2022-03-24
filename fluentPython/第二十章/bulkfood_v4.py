#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

class Quantity:
    __counter = 0  #Quantity类的属性，同济Quantity实例的数量

    def __init__(self):
        cls = self.__class__  #cls是Quantity类的引用
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index) #每个描述符实例storage_name都是独一无二的的
        cls.__counter += 1
    
    #owner参数是托管类（如 LineItem)的引用，通过描述符从托管类中获取属性时用得到
    def __get__(self, instance, owner):  #实现get，因为托管属性的名称与storage_name不同
        if instance is None:
            return self  #如果不是通过实例调用，返回描述符自身
        else:
            return getattr(instance, self.storage_name) #使用内置函数getattr从instance中获取存储属性的值

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value) #使用内置setattr函数把值存储在instance中
        else:
            raise ValueError('Vaule must be > 0')

class LineItem:
    '''
    >>> from bulkfood_v4 import LineItem
    >>> coconuts = LineItem('Brazilian coconut', 20, 17.95)
    >>> coconuts.weight, coconuts.price
    (20, 17.95)
    >> getattr(coconuts, '_Quantity#0')
    20
    '''
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price