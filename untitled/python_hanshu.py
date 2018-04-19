#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# 迭代器与生成器 迭代器有两个基本的方法：iter() 和 next()
# 迭代器是一个可以记住位置的对象

# list = [1,2,3]
# it = iter(list)
# print it
# print next(it)

# for x in it:
#     print x

# 使用了 yield 的函数被称为生成器（generator）
# 生成器是一个返回迭代器的函数，只能用于迭代操作
# 每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行 next()方法时从当前位置继续运行。
# ??????生成器不理解

# m = (i for i in range(0,15))  #range(0,15)  [0,15)
# print m #m 是一个迭代器
# for n in m:
#     print n

# def fab(num):
#     a,b,sum = 0,1,0
#     while sum < num:
#         print b
#         a,b = b,a+b
#         sum = sum+1

# fab(5)

"""---函数---"""
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，
# 而 list,dict 等则是可以修改的对象

# python 传不可变对象
# def change(a):
#     a = 10

# b = 2
# change(b)
# print b

# 传可变对象
# def changename(mylist):
#     mylist.append([2,3,4,5])
#     print "函数内取值：",mylist

# mylist1 = [10,11,12]
# changename(mylist1)
# print "函数外取值：",mylist1

# 必需参数
def printname(str):
    print str

printname(111)

# 关键字参数
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值

def printname2(name,age):
    print "姓名：",name,"年龄：",age
printname2(age=12,name="李四")

# 默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数
def printname3(name,age = 18):
    print "姓名：",name,"年龄：",age
printname3(name="张三")
printname3(name="赵六")
printname3("王五",20)

# 不定长参数
# 可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数
"""
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
加了星号（*）的变量名会存放所有未命名的变量参
如果在函数调用时没有指定参数，它就是一个空元组
"""
def  functionname(arg,*vartuple):
    "不定长参数"
    print arg
    for i in vartuple:
        print i

functionname(10)
functionname(10,20,30)


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(1, 2)
print calc()

"""******匿名函数******"""
# python 使用 lambda 来创建匿名函数
# lambda [arg1 [,arg2,.....argn]]:expression
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果

# sum = lambda a,b:a+b
# print "匿名函数：",sum(10,30)

# 读取键盘输入
# raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）
# input([prompt])可以接收一个Python表达式作为输入，并将运算结果返回
# str = raw_input("请输入内容:")
# print "你输入的内容是：",str

# str = input("请输入：");
# print "你输入的内容是: ", str

