#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from concurrent import futures
from flag import save_flag, get_flag, show, main

MAX_WORKERS = 20

def dwonload_one(cc):  #下载一个图像的函数
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))   #避免创建多余的线程
    #executor.__exit__ 方法会调用executor.shutdown(wait=True) 方法，它会在所有线程都执行完毕前阻塞线程。
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(dwonload_one, sorted(cc_list))
    #map方法的作用与内置的map函数类似，不过download_one函数会在多个线程中并发调用；
    #map方法返回一个生成器，因此可以迭代，获取各个函数返回的值

    return len(list(res)) 
    #返回获取的结果数量；如果有线程抛出异常，异常会在这里抛出，这与隐式调用 next() 函数从迭代器中获取相应的返回值一样。

if __name__ == "__main__":
    main(download_many)