#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

class HauntedBus:

    #默认参数使用一个空列表（可变对象）
    def __init__(self, passengers=[]):
        #创建了默认列表的别名
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)     #结果：['Alice', 'Bill']
bus1.pick('Charlie')    
bus1.drop('Alice')
print(bus1.passengers)     #结果：['Bill', 'Charlie']

#bus使用了默认值空列表
bus2 = HauntedBus()
#给默认的空列表添加值
bus2.pick('Carrie')        #结果：['Carrie']
print(bus2.passengers)

#bus也使用了默认得空列表，与bus2对应的同一个引用，此时默认列表不是空的
bus3 = HauntedBus()
print(bus3.passengers)     #结果：['Carrie']
bus3.pick('Dave')        
print(bus3.passengers)     #结果：['Carrie', 'Dave']
print(bus2.passengers)     #结果：['Carrie', 'Dave']
#bus2和bus3指定的同一个列表
print(bus2.passengers is bus3.passengers)  #结果：True
#bus1是不同的列表
print(bus1.passengers)     #结果：['Bill', 'Charlie']

#__defaults__ 属性
print(HauntedBus.__init__.__defaults__)     #结果：(['Carrie', 'Dave'],)
#验证 bus2.passengers 是一个别名，它绑定到HauntedBus.__init__.__defaults__ 属性的第一个元素上
print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)    #结果：True