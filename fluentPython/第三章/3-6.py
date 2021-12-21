#-*- coding: UTF-8 -*-

a = {'a','b','c','d','e','f','g','h','i',''}
b = {'a','b'}

found = len(a & b)
found = len(set(a) & set(b))
found = len(set(a).intersection(b))