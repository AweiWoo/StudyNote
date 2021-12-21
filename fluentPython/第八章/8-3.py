#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
#浅复制
bus2 = copy.copy(bus1)
#深复制
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))
bus1.drop('Bill')
#passengers是对象中一个可变对象
print(bus2.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
#bus2的Bill对象也被drop了
print(bus2.passengers)
#bus3没有受影响
print(bus3.passengers)
