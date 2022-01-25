#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

class DemoException(Exception):
    """定义的异常类型"""

def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')
