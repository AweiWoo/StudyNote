#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

#示例来自于：https://zhuanlan.zhihu.com/p/179265105

class Displayer:
    def display(self, message):
        print(message)


class LoggerMixin:
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        print(super())
        super().display(message)  #这个地方需要深入理解，为什么会去找Displayer类中的display
        self.log(message)


class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename='subclasslog.txt') 

print(MySubClass.mro())
obj = MySubClass()
obj.display("This string will be shown and logged in subclasslog.txt")