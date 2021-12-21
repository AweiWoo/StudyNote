#-*- coding: UTF-8 -*-
from array import array
from random import random
floats = array('d',( random() for i in range(10**7)))
print(floats[-1])
#把数组存储到一个二禁止文件
fp=open('floats.bin','wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin','rb')
floats2.fromfile(fp,10**7)
fp.close()
print(floats2[-1])
