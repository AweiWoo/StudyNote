#-*- coding: UTF-8 -*-
import timeit
TIMES = 10000
SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    #python3中print成为了一个内置函数：print(value1, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    print(label, *('{:.3f}'.format(x) for x in res))
    #python2中print是一个语法结构
    #print label, [ i for i in ('{:.3f}'.format(x) for x in res)]
       

clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')