"""
Python位运算符
& 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
| 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
^ 按位异或运算符：当两对应的二进位相异时，结果为1
~ 	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1
<< 	左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。
>> 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数

"""

"""
Python逻辑运算符
and 布尔"与" 
   如果 x 为 true，x and y 返回 y 的计算值
   如果 x 或 y为 False，x and y 返回 False
or  布尔"或"	
    如果 x 为 true，它返回 x 的值
    如果 x 是0，它返回 y 的计算值，如果 y 是0，它返回 x 的计算值

not 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True

"""
a = 0
b = 0
# a = 0
# b = 0
# if(a and b):
#     print (a and b)
#     print "a、b都是true"
# else:
#     print (a and b)

if (a or b):
    print(a or b)
    print("a、b都为true，或有一个为true")
else:
    print("a/b都为false")
# if True:
#     print "ddd"
# else:
# print "qq"

"""
Python成员运算符
in  如果在指定的序列中找到值返回 True，否则返回 False
not in 如果在指定的序列中没有找到值返回 True，否则返回 False
"""
a = 1
list = [1, 2, 3, 4]
if (a in list):
    print("变量a在list中")
if (a not in list):
    print("变量a不在list中")

"""
Python身份运算符
身份运算符用于比较两个对象的存储单元
is  是判断两个标识符是不是引用自一个对象
x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False

is not 是判断两个标识符是不是引用自不同对象
x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False

id() 函数用于获取对象内存地址

"""
a = 20
b = 20
if (a is b):
    print("a/b有相同标识")
else:
    print("a/b没有相同标识")

# a = 30
if (a is not b):
    print("a/b没有相同标识")
else:
    # print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
    print("a/b有相同标识")
    # print("a/b有相同标识", a, end="")

    # is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等