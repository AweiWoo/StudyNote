#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import time

DEFAULT_FMT = '[{elapsed:0.8}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):    #参数化装饰器工厂函数
    def decorate(func):        #真正的装饰器
        def clocked(*_args):   #包装被装饰的函数
            t0 = time.time()
            _result = func(*_args)   #被装饰的函数返回的真正结果
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)  #字符串表现形式，用于显示
            #locals() 函数会以字典类型返回当前位置的全部局部变量。
            print(fmt.format(**locals()))  #这里会使用fmt格式化打印除clocked的局部变量
            return _result  #返回被装饰函数的结果，后面clocked会取代被装饰函数
        return clocked  #decorate返回clocked
    return decorate  #clock返回decorate

if __name__ == '__main__':

    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)