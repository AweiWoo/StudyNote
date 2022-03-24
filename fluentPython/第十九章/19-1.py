#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu


class Class:
    data = 'the class data attr' #类属性

    @property
    def prop(self):   #类特性
        return 'the prop value'

#实例属性遮盖类的数据属性
obj = Class()
print(vars(obj))  #{},vars 函数返回 obj 的 __dict__ 属性，表明没有实例属性
print(obj.data) #the class data attr, s实例获取的是 Class.data 的值
obj.data = 'ww'  #创建一个实例属性，属性名与类属性名相同
print(vars(obj)) #{'data': 'ww'}
print(obj.data)  #ww,再次打印实例属性，实例属性掩盖了类属性data
print(Class.data) #Class.data完好无损

#实例属性不会掩盖类特性
print(Class.prop) #<property object at 0x00000226D075ED10>, 特性对象，不会运行特性的读值方法
print(obj.prop) #the prop value, 执行特性的读值方法
#obj.prop = 'foo' #AttributeError: can't set attribute, 尝试设置 prop 实例属性，结果失败
obj.__dict__['prop'] = 'foo'
print(vars(obj)) #{'data': 'ww', 'prop': 'foo'},但是可以直接把 'prop' 存入 obj.__dict__ ,两个实例属性
print(obj.prop) #the prop value, 特性没被实例属性遮盖
Class.prop = 'baz'  #通过类属性复制方式可以覆盖 Class.prop 特性，销毁特性对象
print(obj.prop) # foo， 现在，obj.prop 获取的是实例属性。Class.prop 不是特性了，因此不会再覆盖 obj.prop

#新添加的类特性遮盖现有的实例属性
print(obj.data) # ww , 实例属性
print(Class.data) # the class data attr， 类属性
Class.data = property(lambda self: 'the "data" prop value') #特性覆盖类属性
print(obj.data) #the "data" prop value, obj.data 被 Class.data 特性遮盖了
del Class.data
print(obj.data) #ww, 删除特性，恢复原样。obj.data 获取的是实例属性 data