#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''  #创建一个变量，用于保存可能出现的错误消息
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero'
    finally:
        sys.stdout.write = original_write  #撤销对 sys.stdout.write 方法所做的猴子补丁
        if msg:
            print(msg)
