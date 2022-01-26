#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from collections import namedtuple

Result = namedtuple('Result','count average')

#子生成器
def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield   #main函数中客户端代码发送的值绑定到term变量上
        #重要的终止条件，否则yield from调用的这个协程的生成器会永远阻塞
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)  #返回值会成为grouper函数中yield from表达式的值


#委派生成器:会持续不断的初始化协程对象
def grouper(results, key):
    """
        grouper发送的个值都会经由yield from处理，通过管道传给averager实例。
        grouper会在yield from表达式处暂停，等待averager实例处理客户端发来的值。
        averager实例运行完毕后，返回的值绑定到result[key]上
        while循环会不断的创建averager实例，处理更多的值
        yield from  可以正常的处理异常
    """
    while True:   #这个循环每次迭代都会新建一个averager实例，每个实例都是作为协程适用的生成器对象
        results[key] = yield from average()



#客户端代码，即调用方
def main(data):
    results = {}  #用于收集结果
    for key, values in data.items():
        #group是调用grouper函数得到的生成器对象，group作为协程使用
        group = grouper(results, key) #key如：girls;kg
        next(group)            #预激
        for value in values:   
            group.send(value)   #将key对应的value发送给grouper,grouper委托给averager处理
        group.send(None)  #至关重要，终止当前的averager实例，同时让grouper继续运行
    #print(results)
    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}'.format(result.count, group, result.average, unit))

data = {
    'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':[1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == '__main__':
    """
    执行结果：
    9 boys  averaging 40.42
    9 boys  averaging 1.39
    10 girls averaging 42.04
    10 girls averaging 1.43
    """
    main(data)
