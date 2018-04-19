# -*- coding: utf-8 -*-
# 调试 
# 1、print
# 2、断言
# 凡是用print的地方都可以使用断言（assert）来代替
# 程序中如果到处充斥着assert，和print相比也好不到哪去。
# 不过，启动Python解释器时可以用-O参数来关闭assert python -o 
# 关闭后，你可以把所有的assert语句当成pass来看。
# def foo(s):
#     n = int(s)
#     assert n != 0,'n is zero'
#     return 10/n
# def main():
#     foo('1')
# main()

# 3、logging
# 把print替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
# import logging
# # 添加配置
# logging.basicConfig(level=logging.DEBUG)
# s = '0'
# n = int(s)
# logging.debug('n=%d' % n)
# print 10/n

# 4、pdb python调试器 python -m pdb python_error2.py
# s = '0'
# n = int(s)
# print 10/n

# 输入l 查看代码； n 单步执行； p 变量名 长变量； q 结束调试
# 5、pdb.set_trace()设置断点  先引入模块 import pdb
import pdb
s = '0'
n = int(s)
pdb.set_trace()  #运行到此暂停
print 10/n

