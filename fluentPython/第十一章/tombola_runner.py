#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import doctest

from tombola import Tombola

import bingo, lotto, tombolist

TEST_FILE = 'tombola_tests.rst'  #使用外部文档做测试对象
TEST_MSG = '{0:16} {1.attempted:2} test, {1.failed:2} failed - {2}'

def main(argv):
    verbose = '-v' in argv
    real_subclasses = Tombola.__subclasses__()    #返回抽象基类的直接子类
    virtual_subclasses = list(Tombola._abc_registry)  #返回抽象基类注册的虚拟子类的弱引用（WeakSet对象），3.4版本后貌似已经无法使用

    for cls in real_subclasses + virtual_subclasses:
        test(cls, verbose)


def test(cls, verbose=False):

    res = doctest.testfile(TEST_FILE,
            globs={'ConcreteTombola': cls}, #把cls参数（要测试的类）绑定到全局命名空间里的ConcreteTombola名称上
            verbose=verbose,
            optionflags=doctest.doctest.REPORT_ONLY_FIRST_FAILURE)
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, tag)) #格式输出


if __name__ == '__main__':
    import sys 
    main(sys.argv)