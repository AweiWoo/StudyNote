#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu


#要点：内置类型 dict 的 __init__ 和 __update__ 方法会忽略我们子类写的 __setitem__ 方法

class DoppelDict(dict):
    def __setitem__(sellf, key, value):
        super().__setitem__(key, [value] * 2)


dd = DoppelDict(one=1)
print(dd)  #{'one': 1} ,继承了dict中的构造函数__init__，直接忽略了__setitem__方法

dd['two'] = 2
print(dd) #{'one': 1, 'two': [2, 2]}， []运算符调用__setitem__

dd.update(three=3)  
print(dd)  #{'one': 1, 'two': [2, 2], 'three': 3}， 继承自dict中的update方法也不会使用自己定义的__setitem__方法


#要点：不只实例内部的调用有这个问题，内置类型的方法调用的其他类的方法，如果被覆盖了，也不会被调用。
#dict.update 方法会忽略，AnswerDict.__getitem__ 方法
class AnswerDict(dict):
    def __getitem__(self, key):
        return 42

ad = AnswerDict(a='foo', b='too')
print(ad)    #{'a': 'foo', 'b': 'too'}, 忽略了__getitem__
print(ad['a'], ad['b'])  #42 42 ， 使用这种方式访问，不管传入什么都返回__getitem__定义的值
d = {}
d.update(ad)
print(d['a'])  #foo ， 自定义个字典，用ad填入，忽略了__getitem__方法