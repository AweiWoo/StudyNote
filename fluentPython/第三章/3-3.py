#-*- coding: UTF-8 -*-

#定义一个类，继承dict类
class StrKeyDict0(dict):

    #如果找不到的键本身是字符串，抛出keyerror错误，如果不是字符串，那么转换为字符串。
    def __missing__(self,key):
        #这个isinstance是非常必要的，如果没有，则当寻找一个不存在的键时候，会陷入无限递归。getitem->missing->getitem-missing...
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]
    #get方法把查找工作用self[key]的方式委托给__getitem__
    def get(self,key,default=None):
        try:
            return self[key]
        #如果抛出keyerror错误，那么说明__missing__也失败了，返回default
        except KeyError:
            return default
    def __contains__(self,key):
        #先使用原本键值查找，再使用转为字符串后的值查找
        #这里没有k in my_dict来检查键是否存在，这样会导致__contains__被递归调用
        return key in self.keys() or str(key) in self.keys()

#这里传入是一个列表，为什么会转化为映射类型？？？
d = StrKeyDict0([('2','two'),('4','four')])
print(d['2'])
#2在d对象中不存在，但是仍然可以返回"two",因为调用了__missing__方法，谁调用的呢，当然是父类中的__getitem__调用的
print(d[2])
#1不存在，转为str也找不到，返回keyerr错误
print(d[1])

print(d.get('2'))
#get方法查找使用了self[key]，依然会使用到__missing__方法
print(d.get(2))
print(d.get(1))

# k in d这个操作不会调用__missing__方法，所以这里我们自己实现
print('2' in d)
print(1 in d)