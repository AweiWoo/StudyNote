#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from array import array
import reprlib 
import math
import numbers
import functools
import operator

class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        #使用过一个属组，将多维向量的各个分量保存在一个数组中
        self._components = array(self.typecode, components)

    def __iter__(self):
        #构建一个迭代器
        return iter(self._components)

    def __repr__(self):
        #reprlib支持有限长度的展示
        components = reprlib.repr(self._components)
        #去掉前面的array('d' 和后面的 )
        #find函数可以找到所查找的内容对于的所以位置
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        #return tuple(self) == tuple(other)
        #两个对象长度不相等，直接返回False
        if len(self) != len(other):
            return False
        #通过zip函数生成一个由元组构成的生成器，逐个对比
        for a, b in zip(self, other):
            if a != b:   #出现有一个不一样就返回False
                return False
        return True
        #使用归约函数一行表达：
        #return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        #创建一个生成器表达式，惰性计算各个分量的散列值。
        #hashes = (hash(x) for x in self._components)
        hashes = map(hash, self._components)
        #把 hashes 提供给 reduce 函数，使用 xor 函数计算聚合的散列值；第三个参数，0 是初始值
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        #先计算各分量的平方之和，然后再使用 sqrt 方法开平方
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        #直接把 memoryview 传给构造方法，不用像前面那样使用 * 拆包
        return cls(memv)

    #实现序列协议，让其可以支持切片操作
    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        #获取实例所属类（Vector）
        cls = type(self)
        #r如果index参数值是slice对象
        if isinstance(index, slice):
            #调用构造方法，使用 _components 数组的切片构建一个新 Vector 实例。
            return cls(self._components[index])
        #如果 index 是 int 或其他整数类型
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))
    
    def __getattr__(self, name):
        cls = type(self)  #获取vector
        #如果属性名只是一个字母，且必须是shortcut_names中的一个
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            #保证shortcut_names中获取的字符在序列范围内，返回数组中的元素
            if 0<= pos < len(self._components):  
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        #特别处理名称时单个字符的属性
        if len(name) == 1:
            # 如果 name 是 xyzt 中的一个，设置特殊的错误消息
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        #不存在上面情况，默认情况下调用超类中的__setattr__
        super().__setattr__(name, value)

        

