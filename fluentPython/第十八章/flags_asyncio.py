from email import header

#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import asyncio

import aiohttp

from flag import BASE_URL, save_flag, show, main

@asyncio.coroutine
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    # 阻塞的操作通过协程实现，把职责委托给aiohttp.request协程，异步运行协程
    #resp = yield from aiohttp.request('GET', url)
    resp = yield from aiohttp.ClientSession().get(url)
    # 读取响应内容是一项单独的异步操作。
    image = yield from resp.read()
    return image
 
@asyncio.coroutine
def download_one(cc):
    image = yield from get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    # 获取一个事件循环对象，用来处理调用download_one函数生成的协程对象
    loop = asyncio.get_event_loop()
    # 构建一个生成器对象列表
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    # wait 是一个协程，等传给它的所有协程运行完毕后结束，名称是wait，但并不阻塞
    wait_coro = asyncio.wait(to_do)
    # 执行事件循环，直到wait_coro结束，此过程脚本会阻塞。
    res, _ = loop.run_until_complete(wait_coro) #第二个元素是一系列未结束的future
    loop.close() #关闭事件循环
    return len(res)

if __name__ == '__main__':
    main(download_many)