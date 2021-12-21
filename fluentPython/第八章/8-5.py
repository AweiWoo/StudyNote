#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import weakref

class Cheese:

    def __init__(self, kind):
        self.kind  = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

#创建一个映射类型的弱引用
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

#将catalog中的对象放入stock中，其中key为Cheese类的kind属性，value为元素值（具体的类对象）
for cheese in catalog:
    stock[cheese.kind] = cheese
for s in stock.items():
    print(s)                     #('Red Leicester', Cheese('Red Leicester'))
print(sorted(stock.keys()))      #['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']

#删除catalog后发现大部分元素都不见了，但是还剩下最后一个，
#因为for 循环中的变量 cheese 是全局变量，除非显式删除，否则不会消失。
del catalog
print(sorted(stock.keys()))   #['Parmesan']

#显示删除cheese
del cheese
print(sorted(stock.keys()))  #依然剩下['Parmesan']，因为还有一个for循环

#显示删除s
del s
print(sorted(stock.keys())) 