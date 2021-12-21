#-*- coding: UTF-8 -*-

import bisect
import random

SIZE=7
#seed()方法改变随机数生成器的种子,不是很好理解，感觉设置了这个生成的随机数是固定的
#如果不设置这个，每次执行的都结果不一样
random.seed(1729)

my_list= []
for i in range(SIZE):
    #randrange() 方法返回指定递增基数集合中的一个随机数，基数默认值为1。
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list,new_item)
    print('%2d ->' % new_item,my_list)