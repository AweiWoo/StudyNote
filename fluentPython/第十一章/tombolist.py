#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from random import randrange
from tombola import Tombola

@Tombola.register       #把TomboList注册为Tombola的虚拟子类
class TomboList(list):  #TomboList继承了list,是list的实体子类

    def pick(self):
        if self:    #从list中继承了__bool__方法，这样就不用try语句了
            position = randrange(len(self))
            return self.pop(position)  #调用继承自list的self.pop方法
        else:
            raise LookupError('pop from empty TombolaList')

    load = list.extend #load得到是一个方法对象，类似于TomboList.load

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))