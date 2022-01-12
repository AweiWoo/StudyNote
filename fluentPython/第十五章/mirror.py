#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

class LookingGlass:

    def __enter__(self):  #不传入其他参数
        import sys
        self.original_write = sys.stdout.write #把本来的sys.stdout.write方法保存在一个实例属性中，供后面使用
        sys.stdout.write =  self.reverse_write #重新实现一个sys.stdout.write方法，属于打猴子补丁
        return 'JABBERWOCKY'   #使用with的时候又传入的内容

    def reverse_write(self, text):   
        self.original_write(text[::-1]) #把 text 参数的内容反转，然后调用原来写入方法的实现
    
    #退出时的操作，如果一切正常，Python 调用 __exit__ 方法时传入的参数是 None,None, None；如果抛出了异常，这三个参数是异常数据
    def __exit__(self, exc_type, exc_value, traceback):  
        import sys    #重复导入模块不会消耗很多资源，因为 Python 会缓存导入的模块
        sys.stdout.write = self.original_write  #还原成原来的sys.stdout.write方法
        if exc_type is ZeroDivisionError:  #如果有异常，而且是 ZeroDivisionError 类型，打印一个消息…
            print('Please DO NOT divide by zero!')
            return True  #返回 True，告诉解释器，异常已经处理了
        #if exc_value 
        #if traceback