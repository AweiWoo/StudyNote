#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from concurrent import futures
from flag import save_flag, get_flag, show, main

MAX_WORKERS = 20

def donwload_one(cc):  #下载一个图像的函数
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    cc_list = cc_list[:5]   #只下载5个对象
    with futures.ThreadPoolExecutor(max_workers=3) as executor:  
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(donwload_one, cc)
            to_do.append(future)   #存储各个future,传给后面的futures.as_completed
            msg = 'Scheduled for {} : {}'
            print(msg.format(cc, future))
        
        results = []
        for future in futures.as_completed(to_do):
            res = future.result()   #获取future结果
            msg = '{} result: {!r}'
            print(msg.format(future, res))  #显示结果
            results.append(res)

    return len(results)


if __name__ == "__main__":
    main(download_many)