#-*- coding: UTF-8 -*-
#hypot() 返回欧几里德范数 sqrt(x*x + y*y), 即求平方根。
from math import hypot

class Vector:
    #构造函数
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    #实现此特殊方法，则可以将Vector对象以字符串形式表示出来
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    #此特殊方法会优先使用
    # def __str__(self):
    #     return 'aaaa(%r, %r)' % (self.x, self.y)

    #实现此特殊方法，则Vector对象可以实现内置函数abs()运算。
    #如果输入的是整数或浮点数则返回绝对值。
    #若参数为复数，则返回复数的绝对值（此复数与它的共轭复数的乘积的平方根），就是 (x^2+y^2) 开根。
    def __abs__(self):
        #利用math的pypot方法来实现平方根运算
        return hypot(self.x, self.y)

    #实现此特殊方法，则实现了bool运算
    #默认情况下，自定义的类的实例总被认为是真的，除非这个类对__bool__或者__len__函数有自己的实现
    def __bool__(self):
        return bool(abs(self))
        #return bool(self.x or self.y)

    #实现此特殊方法，则实现了向量的加法运算
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    #实现此特殊方法，则实现向量的乘法运算
    def __mul__(self,scale):
        return Vector(self.x * scale, self.y * scale)

v=Vector(3,4)
print abs(v)
print v
print str(v)
#没有实现__repr__方法，输出结果为：<__main__.Vector instance at 0x0000000002CB9248>
#实现了__repr__方法，输出结果为：Vector(3, 4)
print Vector(3,4) + Vector(4,5)
print v*3
print bool(v)