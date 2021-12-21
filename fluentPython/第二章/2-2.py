#-*- coding: UTF-8 -*-
import bisect
import sys

#bisect 模块包含两个主要函数（ bisect 和 insort），它们内部利用二分查找算法，分别用于在有序序列中查找元素与插入元素。

HAYSTACK = [1,3,5,6,7,8,12,45,23,67]
NEEDLES = [0,1,2,3,4,10,20,30]

#输出格式:https://www.runoob.com/python/att-string-format.html
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        #找出插入的位置
        position = bisect_fn(HAYSTACK,needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle,position,offset))

if __name__ == '__main__':
    #从右边数第一个参数
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    
    print('DEMO',bisect_fn.__name__)
    print('haystack ->',' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

#知识点：
# 1、bisect模块
# 2、字符串格式化输出，str.format和%方式