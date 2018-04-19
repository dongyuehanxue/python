# print "hello world"
#coding=utf-8

# 一般以新行作为为语句的结束符，也可以使用斜杠（ \）将一行的语句分为多行显示
# Python 可以使用引号( ' )、双引号( " )、三引号( ''' / """ ) 来表示字符串

# 中文编码  # -*- coding：UTF-8  或 #coding=utf-8
# 注释 单行注释采用 # 开头  多行注释使用三个单引号(''')或三个双引号(""")

"""
标识符由字母、数字、下划线组成
标识符是区分大小写
以下划线开头的标识符是有特殊意义的
Python 中的变量赋值不需要类型声明
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建

Python有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）

可以使用del语句删除一些对象的引用
del var_a, var_b

Python支持四种不同的数字类型：
int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）
float（浮点型）
complex（复数）
长整型也可以使用小写 l，但是还是建议您使用大写 L，避免与数字 1 混淆。Python使用 L 来显示长整型。
"""
# print "ffff"
# print "11", "22"
#
# name = "李四"
# age = 23
#
# a, b, c = 1, 2, "john"
# del a
# print b,c
# print name,age

"""Python提供了一个raw_input，可以让用户输入字符串，并存放到一个变量里
在python2.x中raw_input()和input( )，两个函数都存在，其中区别为：
 raw_input()---将所有输入作为字符串看待，返回字符串类型
 input()-----只能接收"数字"的输入，在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（int, float ）
在python3.x中raw_input()和input( )进行了整合，去除了raw_input()，仅保留了input()函数，
其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。"""
# name = input('请输入你的名字：')
# print('hello,',name,'!')

"""空值是Python里一个特殊的值，用None表示。
None不能理解为0，因为0是有意义的，而None是一个特殊的空值"""

"""python的字串列表有2种取值顺序:
从左到右索引默认0开始的，最大范围是字符串长度少1
从右到左索引默认-1开始的，最大范围是字符串开头
"""
# s = "12345678"
# print s     # 输出完整字符串
# print s[0]  # 输出字符串中的第一个字符
# print s[2:5]# 输出字符串中第三个至第五个之间的字符串
# print s[2:] # 输出从第三个字符开始的字符串
# print s*2   # 输出字符串两次
# print s + "test" # 输出连接的字符串

"""
List（列表） 是 Python 中使用最频繁的数据类型  相当于JAVA中的数组
列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）
列表用 [ ] 标识，是 python 最通用的复合数据类型
列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，
从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
加号 + 是列表连接运算符，星号 * 是重复操作
"""
# person = ["张三",25,"职员"]
# print  person
# print person[0]
# print person[:2]

"""用len()函数可以获得list元素的个数
list是一个可变的有序表，所以，可以往list中追加元素到末尾 .append()
把元素插入到指定的位置，比如索引号为1的位置 .insert()
删除list末尾的元素，用pop()方法


"""

# person = ["张三",25,"职员"]
# print(len(person))

# # 添加列表
# person.append('地址')
# print(person)

# person.insert(1,'男')
# print(person)

# # 删除
# person.pop()
# print(person)

# num = ['hi!']*4
# print(num)
# del num[2]
# print(num)
# # 截取
# print(person[0:2])
"""
Python元组
元组是另一个数据类型，类似于List（列表）。 
元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表
"""
zoom = ("www","11")
# print zoom

"""元组是不允许更新的。而列表是允许更新"""
#
# zoom[0] = "eee"
# print zoom(0)
# person[1] = 30
# print person[1]

for a in zoom:
    print a

"""
Python 字典   相当于JAVA中的对象
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型
列表是有序的对象集合，字典是无序的对象集合
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
字典用"{ }"标识。字典由索引(key)和它对应的值value组成
"""
# dict  = {}
# dict['one'] = "this is one"
# dict[3] = "3333"
tinydict = {'name':'Bob','age':24}
# print dict['one']
# print dict[3]
# print tinydict # 输出完整的字典
# print tinydict.keys() # 输出所有键
# print tinydict.values() # 输出所有值
# print tinydict['name']

# for i in tinydict:
#     print i
# print([a for a in tinydict])

"""在 python 用 import 或者 from...import 来导入相应的模块
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
"""

#除法（/）总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符 //
# print(3/2)

"""Python字符串格式化
Python 支持格式化字符串的输出 
%s 字符串 %d 整数
"""
# print("姓名：%s,年龄：%d"%("小米",10))

"""python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符"""

# HTML= """<html>
#     <head>html</head>
#     <body>主\t体\n</body>
# </html>"""
# print(HTML)

"""在Python3中，所有的字符串都是Unicode字符串"""
# var1 = "hello world"
# print(var1[3: 7]) #【3,7） 从3开始到7之前
#
# num = 10
# print("十六进制：%#x"%num)
# print("八进制：%#o"%num)
# print("二进制：",bin(num))