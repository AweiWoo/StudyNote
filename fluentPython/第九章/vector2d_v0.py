from array import array
import math

class Vector2d:

    __slots__ = ('__x', '__y')

    typecode = 'd'

    def __init__(self, x, y):
        #将x, y设置为私有属性
        self.__x = float(x)
        self.__y = float(y)

    @property     #@property装饰器把读值方法标记为特性
    def x(self):   #读值方法与公开属性同名，都是x
        return self.__x

    @property   #Vector.x 和 Vector.y 是只读特性。
    def y(self):
        return self.__y

    def __iter__(self):
        #通过 self.x 和self.y 读取公开特性，而不必读取私有属性
        return (i for i in (self.x, self.y))  

    def __hash__(self):
        #使用位运算符异或（^）混合各分量的散列值
        return hash(self.x) ^ hash(self.y)

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    #类方法使用classmethod装饰器
    @classmethod
    def frombytes(cls, octets):     #不传入self参数，传入类本身(cls)
        typecode = chr(octets[0])  #获取第一个字节，第一个字节表示的是typecode
        #将第一个字节后面的序列放入到一个memoryview，使用cast进行转换
        memv = memoryview(octets[1:]).cast(typecode) 
        # 拆包转换后的 memoryview，得到构造方法所需的一对参数。
        return cls(*memv)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        #计算角度
        return math.atan2(self.x, self.y)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):  #如果代码一'p'结尾，使用极坐标
            fmt_spec = fmt_spec[:-1]  #从fmt_spec中删除p
            coords = (abs(self), self.angle())  # 构建一个元组，表示极坐标：(magnitude, angle)。 
            outer_fmt = '<{}, {}>' #把外层格式设为一对尖括号。
        else:
            coords = self  # 如果不以 'p' 结尾，使用 self 的 x 和 y 分量构建直角坐标
            outer_fmt = '({}, {})' #把外层格式设为一对圆括号。
        components = (format(c, fmt_spec) for c in coords) #使用各个分量生成可迭代的对象，构成格式化字符串
        return outer_fmt.format(*components) #把格式化字符串代入外层格式


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    #直接通过属性访问
    print(v1.x, v1.y)  #3.0 4.0
    #实例可以拆包
    x, y = v1
    print(x, y)    #3.0 4.0
    #print函数调用__str__函数
    print(v1)     # (3.0, 4.0)
    #eval是Python的一个内置函数，这个函数的作用是，返回传入字符串的表达式的结果，
    #即变量赋值时，等号右边的表示是写成字符串的格式，返回值就是这个表达式的结果。
    v1_clone = eval(repr(v1))
    print(v1_clone)
    print(v1 == v1_clone)
    octets = bytes(v1)
    print(octets)
    print(abs(v1))
    print(bool(v1), bool(Vector2d(0, 0)))