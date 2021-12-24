#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import decimal
ctx = decimal.getcontext()         #获取当前全局算术运算上下文引用，可以输出看到默认精度为28
ctx.prec = 40                      #把精度设置为40
one_third = decimal.Decimal('1') / decimal.Decimal('3') #进行计算
print(one_third)                   #0.3333333333333333333333333333333333333333， 得到40精度的结果
print(one_third == +one_third)     #True， 此时one_third与取正向运算结果相等

ctx.prec = 28                      #将精度改为28
print(one_third == +one_third)     #False,one_third为40精度， 而去正向运算后精度变为28
print(+one_third)                  #0.3333333333333333333333333333

#结论：在变量的上下文环境发生变化时候，可能导致 x 与 +x 不相等