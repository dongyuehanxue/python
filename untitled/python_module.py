#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 在Python 2.7的代码中直接使用Python 3.x的除法，可以通过__future__模块的division实现
from __future__ import division

"a test module"

__author__ = "lulu"

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print 'hello'
    elif len(args) == 2:
        print 'hello,%s' % args[1]
    else:
        print 'too many arguments'

# 私有（private _xx __xx）、公开（public）函数和变量
def _private_1(name):
    return 'hello,%s' % name
def _private_2(name):
    return 'hi,%s' % name
def greeting(name):
    if len(name) > 3:
        print(_private_1(name))
    else:
        print(_private_2(name))


# if __name__ == "__main__":
#     test()
#     greeting('zhang')

# 安装第三方库
# Python Imaging Library这是Python下非常强大的处理图像的工具库 PIL

import Image
im = Image.open('python.png')
print im.format,im.size,im.mode

# Python提供了__future__模块，把下一个新版本的特性导入到当前版本
# 在2.7版本的代码中，可以通过unicode_literals来使用Python 3.x的新的语法

# 在Python 2.x中，对于除法有两种情况，如果是整数相除，结果仍是整数，余数会被扔掉，这种除法叫“地板除
# 要做精确除法，必须把其中一个数变成浮点数
# 而在Python 3.x中，所有的除法都是精确除法，地板除用//表示：

print '10/3=',10/3
print '10.0/3',10.0/3
print '10//3',10//3
