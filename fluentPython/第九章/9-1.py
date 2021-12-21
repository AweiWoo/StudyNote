#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

class Demo:
    
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args

print(Demo.klassmeth())      #(<class '__main__.Demo'>,)
print(Demo.klassmeth('adb'))  #(<class '__main__.Demo'>, 'adb')

print(Demo.statmeth())       #()
print(Demo.statmeth('abc'))  #('abc',)