#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

def quantity():
    try:
        #不能依靠类属性在多次调用之间共享 counter，因此把它定义为 quantity 函数自身的属性。
        quantity.counter += 1
    except AttributeError:
        quantity.counter = 0
    
    #利用闭包保持状态
    storage_name = '_{}:{}'.format('quantity', quantity.counter)

    def qty_getter(instance):
        return getattr(instance, storage_name)

    def qty_setter(instance, value):
        if value > 0:
            setattr(instance, storage_name, value)
        else:
            raise ValueError('Value must be > 0')
    
    return property(qty_getter, qty_setter)