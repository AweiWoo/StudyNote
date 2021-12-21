#-*- coding: UTF-8 -*-
import bisect

def grade(score,breakpoints=[60,70,80,90],grades='FDCBA'):
    i = bisect.bisect(breakpoints,score)
    #str中的内置方法：__getitem__
    return grades[i]
s = [grade(score) for score in [33,99,77,70,89,90,100]]
print(s)