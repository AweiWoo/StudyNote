#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from collections import abc
import keyword

#FrozenJSON 类能读取属性，如name，还能调用方法，如 .keys() 和 .items()
class FrozenJSON:
    """
    一个只读接口,使用属性表示访问JSON类对象
    """
    def __init__(self, mapping):
        #定义一个实例属性，构建一个字典。这么做有两个目的：(1) 确保传入的是字典（或者是能转换成字典的对象）；(2) 安全起见，创建一个副本
        #self.__data = dict(mapping) 
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):    #防止JSON对象中的key为python关键字，比如：“class”
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):  #关键，尝试获取其他属性会触发解释器调用 __getattr__ 方法。
        if hasattr(self.__data, name): #先查看self.__data 字典有没有指定名称的属性（不是键）
            return getattr(self.__data, name)
        else:
            try:
                return FrozenJSON.build(self.__data[name]) #重新返回一个类对象
            except KeyError as e:   #理论上，尝试读取不存在的属性应该抛出 AttributeError异常。
                raise AttributeError(e) 
    
    @classmethod   #作用是实现“备选构造方法”
    def build(cls, obj):  #使用类方法把每一层嵌套转换成一个FrozenJSON实例。
        if isinstance(obj, abc.Mapping): #如果obj是字典，就构建一个FrozenJSON对象
            return cls(obj)  
        elif isinstance(obj, abc.MutableSequence): #如果是列表,递归地传给.build() 方法，构建一个列表
            return [cls.build(item) for item in obj]
        else:
            return obj #如果既不是字典也不是列表，那么原封不动地返回元素

if __name__ == "__main__":
    from osconfeed import load
    faw_feed = load()
    feed = FrozenJSON(faw_feed)
    print(feed.Schedule.conferences[0].a)