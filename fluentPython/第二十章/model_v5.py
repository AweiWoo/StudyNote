#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import abc

#自动管理存储属性描述符类
class AutoStorage:  
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix =cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

#扩展AutoStorage类
class Validated(abc.ABC, AutoStorage): #抽象子类，也继承于AutoStorage

    def __set__(self, instance, value):  #覆盖__set__方法
        value = self.validate(instance, value) #__set__ 方法把验证操作委托给 validate 方法
        super().__set__(instance, value) #把返回的 value 传给超类的 __set__ 方法，存储值

    @abc.abstractmethod  #定义一个抽象方法，必须由子类实现
    def validate(self, instance, value):
        """return validated value or raise ValueError"""

class Quantity(Validated):  #继承Validated类，实现一种验证
    """a number greater than zero"""

    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('value must be > 0')
        return value

class NonBlank(Validated): #继承Validated类，实现另一种验证
    """a string with at least one non-space character"""

    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value cannot be empty or blank')
        return value
