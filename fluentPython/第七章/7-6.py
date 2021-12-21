#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch  #@singledispatch标记处理object类型的基函数
def htmlize(obj):
    content =  html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)  #各个专门函数使用@<base_function>.register(<type>)装饰
def _(text):  #专门的函数的名称无关紧要，可以使用“_”
    content = html.escape(text).replace('\n','<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)  #为每种特殊的类型注册一个函数。numbers.Integral 是Int类型的超类（父类）
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)  ##可以叠放多个装饰器，让同一个函数支持不同类型
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'