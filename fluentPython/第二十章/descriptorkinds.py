#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

def cls_name(ojb_or_cls):
    cls = type(ojb_or_cls)
    if cls is type:
        cls = ojb_or_cls
    return cls.__name__.split('.')[-1]

def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))

def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))

#有 __get__ 和 __set__ 方法的典型覆盖型描述符
class Overriding: 
    """也称数据描述符或强制描述符"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)

#没有 __get__ 方法的覆盖型描述符
class OverridingNoGet:
    """没有__get__方法覆盖型描述符"""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)

#没有 __set__ 方法，所以这是非覆盖型描述符
class NonOverriding:
    """也称非数据描述符或遮盖型描述符"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

#托管类
class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))
if __name__ == '__main__':
    obj = Managed()
    obj.over

