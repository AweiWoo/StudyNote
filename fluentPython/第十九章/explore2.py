#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from collections import abc
import keyword

class FrozenJSON:

    def __new__(cls, arg): #类方法，第一个参数是类本身，其他参数与__init__一样，没有self
        if isinstance(arg, abc.Mapping):
            #__new__ 方法的第一个参数是类，因为创建的对象通常是那个类的实例。
            return super().__new__(cls) #默认委托给超类的__new__方法，唯一的参数设置为FrozenJSON
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg
        
    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name]) #这个地方只需要调用FrozenJSON的构造方法
