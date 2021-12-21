#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import abc

class Tombola(abc.ABC): #自定义抽象基类要继承abc.ABC

    @abc.abstractmethod       #使用装饰器定义抽象方法，抽象方法不做任何实现
    def load(self, iterable):
        """向可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回
           如果实例为空，则抛出LookupEror错误
        """

    def loaded(self):
        """如果至少有一个元素，返回True,否则返回False"""
        return bool(self.inspect())    #抽象基类定义的方法只能依赖抽象方法自己定义的接口（自己实现的具体和抽象方法、特性）


    def inspect(self):
        """返回一个有序元组，由当前元素构成"""
        items = []
        #我们不知道具体子类如何存储元素，但为了得到当前结果，可以不断调用抽象方法pick,把Tombola清空。
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        #然后使用抽象方法load把所有元素放回去
        self.load(items)
        return tuple(sorted(items))
