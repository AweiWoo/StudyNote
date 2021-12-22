#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

class A:
    def ping(self):
        print('ping', self)

class B(A):
    def pong(self):
        print('pong', self)

class C(A):
    def pong(self):
        print('PONG', self)

class D(B, C):    #继承类参数的顺序很重要，决定__mro__的顺序
    def ping(self):
        super().ping()
        #如果要绕开__mro__属性，可以直接使用某个超类的方法，如下，需要显示传入self
        #A.ping(self) 
        print('post-ping:', self)

    def pingpong(self):
        self.ping()     #运行D类的ping方法，D类ping委托给A
        super().ping()  #跳过D类ping方法，直接调用A类ping方法
        self.pong()     #调用自己的pong方法,自己没有去超类寻找，遵循__mro__顺序，找到的B类的pong方法
        super().pong()  #直接找超类中的pong(),依然遵循__mro__顺序，找到的B类的pong方法
        C.pong(self)    #直接显示指定超类pong方法，忽略__mro__顺序


if __name__ == '__main__':
    d = D()
    d.pong()  #pong <__main__.D object at 0x0000023EC8DB8FA0>,默认调用了B类中的pong方法
    C.pong(d) #PONG <__main__.D object at 0x0000018D27778FA0>，直接通过超类显示调用，将实例d作为参数传入
    print(D.__mro__)
    #(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
    #根据__mro__方法提供的超类顺序进行调用
    print('----------------------')
    d.ping() 
    #ping <__main__.D object at 0x000001C33C368FA0> , super()遵从__mro__顺序，A.ping()输出
    #post-ping: <__main__.D object at 0x000001C33C368FA0>
    print('------------------------')
    d.pingpong()
    #ping <__main__.D object at 0x0000022D25AC8FA0>
    #post-ping: <__main__.D object at 0x0000022D25AC8FA0>
    #ping <__main__.D object at 0x0000022D25AC8FA0>
    #pong <__main__.D object at 0x0000022D25AC8FA0>
    #pong <__main__.D object at 0x0000022D25AC8FA0>
    #PONG <__main__.D object at 0x0000022D25AC8FA0>