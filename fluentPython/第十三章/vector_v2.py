#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from array import array
import reprlib 
import math
import itertools
import numbers

class Vector:
    """
    >>> from vector_v2 import Vector
    >>> v1 = Vector([3, 4, 5]) 
    >>> v1
    Vector([3.0, 4.0, 5.0])
    >>> -v1
    Vector([-3.0, -4.0, -5.0])
    >>> +v1
    Vector([3.0, 4.0, 5.0])
    >>>
    """

    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __iter__(self):
        return iter(self._components)

    def __len__(self):
        return len(self._components)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        if isinstance(other, Vector):
            return len(self) == len(other) and all(a == b for a, b in zip(self, other))
        else:
            return NotImplemented

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        try:
            #生成 (a, b) 形式的元组,如果 self 和 other 的长度不同，使用fillvalue 填充较短的那个可迭代对象
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)  #生成器
            return Vector(a+b for a, b in pairs)  #一个新 Vector 实例，而没有影响 self 或other
        except TypeError:
            return NotImplemented
    
    def __radd__(self, other):
        return self + other  #直接委托给__add__, 因为使用了 

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real): #类型判断，白鹅类型
            return Vector(n * scalar for n in self)
        else:
            return NotImplemented
            #返回 NotImplemented，Python会尝试在 scalar 操作数上调用 __rmul__ 方法

    def __rmul__(self, scalar):
        return self * scalar

    def __matmul__(self, other):
        try:
            return sum(a * b for a, b in zip(self, other))
        except TypeError:
            return NotImplemented

    def __rmatmul__(self, other):
        return self * other