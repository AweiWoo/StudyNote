#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

def deco(func):
    def inner():
        print('running inner()')
        #func()
    return inner

@deco
def target():
    print('running target()')

target()