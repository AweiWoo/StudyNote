#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):   #定义自定义的 reverse_write 函数
        original_write(text[::-1]) #在闭包中可以访问original_write
    
    sys.stdout.write = reverse_write
    # 产出一个值，这个值会绑定到 with 语句中 as 子句的目标变量上。执行 with 块中的代码时，这个函数会在这一点暂停
    yield 'JABBERWOCKY'
    # 控制权一旦跳出 with 块，继续执行 yield 语句之后的代码；恢复成原来的 sys. stdout.write 方法
    sys.stdout.write = original_write