#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu
# 功能：通过线程以动画形式显示文本式指针旋转

import threading
import itertools
import time
import sys

class Signal:   #定一个简单的可变对
    go = True   #一个属性用于从外部控制线程

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):  #无限循环，从itertools.cycle指定的序列中反复提前对象，\\有一个是转义符
        status = char + ' ' + msg
        write(status)  #write与print的区别就是去掉了默认的换行符，即end参数
        flush()  #保证立即从换从前中输出
        write('\x08' * len(status)) #\x08表示退格，把光标移动回来 
        time.sleep(.1)
        if not signal.go:  #跳出循环的条件
            break
    write(' ' * len(status) + '\x08' * len(status)) #使用空格清楚消息状态，把光标移到开头

def slow_function():
    #假装等待I/O一段时间
    time.sleep(5)   #sleep函数会阻塞主线程，释放GIL,创建从属线程
    return 42

def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    print('spinner object:', spinner)
    spinner.start() #启动从属线程
    #time.sleep(10)
    result = slow_function()
    signal.go = False #主线程给从线程发消息？
    spinner.join()  #join方法会等待从属线程结束再执行其他线程
    return result

def main():
    result = supervisor()
    print('Answer:', result)

if __name__ == '__main__':
    main()