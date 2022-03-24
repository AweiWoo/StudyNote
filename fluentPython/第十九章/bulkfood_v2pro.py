#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

def quantity(storage_name):

    def qty_getter(instance):   #instance表示属性存储的实例
        #直接从__dict__中获取，跳过特性，防止无限递归（了解obj.attr的查找顺序）
        return instance.__dict__[storage_name]  #storage_name保存再函数的闭包中

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError("Value must be > 0")
    #使用property对象包装qty_getter和qty_setter函数，用了老式的property表达方式。
    return property(qty_getter, qty_setter)  #会从闭包中读取storage_name


class LineItem:
    #记住：赋值语句的右边先计算，因此调用quantity()时，weight类属性还不存在
    weight = quantity('weight') #这一行输入两次‘weight’
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight   #这里特性以及激活，确保不把weight设置为复数或0
        self.price = price

    def subtotal(self):
        return self.weight * self.price


nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
print(nutmeg.weight, nutmeg.price)
print(vars(nutmeg).items())