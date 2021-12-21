#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

registy = []

#这是一个没有内部函数的装饰器
def register(func):  
    print('running register(%s)' % func)
    registy.append(func)
    return func

@register
def f1():
    print('running f1()')


def main():
    print('---------------这里才开始执行main函数--------------------')
    print('registy: ' , registy)
    f1()

if __name__ == '__main__':
    main()