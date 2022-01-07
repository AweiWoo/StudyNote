#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')

#列表推导迫切地迭代 gen_AB() 函数生成的生成器对象产出的元素：'A' 和 'B'。
res1 = [ x*3 for x in gen_AB() ]  #注意，没有print，这里就输出start、continue 和 end。
#使用for循环，输出AA，BBB
for i in res1:
    print(i)

res2 = ( x*3 for x in gen_AB() )
print(res2)  #<generator object <genexpr> at 0x000001F390EBF9E0>

for i in res2:
    print('--->', i)
