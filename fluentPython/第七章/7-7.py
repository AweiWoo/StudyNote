#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

registy = set()

def register(active=True):
    def decorate(func):    #这个内部函数才是真正的装饰器，注意，它的参数是一个函数
        print('running register(active=%s) ->decorate(%s)' % (active, func))
        if active:  #只有 active 参数的值（从闭包中获取）是 True 时才注册 func
            registy.add(func)
        else:
            registy.discard(func)
        return func #decorate 是装饰器，必须返回一个函数。
    return decorate   #register 是装饰器工厂函数，因此返回 decorate


@register(active=True)
def f1():
    print('running f1')

@register()
def f2():
    print('running f2')

def f3():
    print('running f3')