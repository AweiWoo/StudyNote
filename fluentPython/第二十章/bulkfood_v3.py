#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

class Quantity: #描述符基于协议实现，无需创建子类

    def __init__(self, storage_name):
        self.storage_name = storage_name #托管实例中存储值的属性的名称。

    #为托管属性赋值，会调用__set__, self是描述符实例（LineItem.weight）
    def __set__(self, instance, value): #instance是托管实例（即：LineItem实例），value为要设定的值
        if value > 0:
            #必须直接处理托管实例的__dict__属性
            #使用内置的setattr函数，会再次触发__set__方法，导致无限递归
            instance.__dict__[self.storage_name] = value 
        else:
            raise ValueError('Value must be > 0') 

class LineItem:
    weight = Quantity('weight') #描述符实例绑定给weight
    price = Quantity('price')  #描述符实例绑定给price

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price