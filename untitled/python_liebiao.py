#coding=utf-8
# 列表推导式
# 每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
# 返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。
# 如果希望表达式推导出一个元组，就必须使用括号

vec = [2,4,6]
print [3*x for x in vec]
print [3*x for x in vec if x>3]

# 嵌套列表
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 将3X4的矩阵列表转换为4X3列表
print "将3X4的矩阵列表转换为4X3列表:",[[row[i] for row in matrix] for i in range(4)]

# trans = []
# for i in range(4):
#     trans.append([row[i] for row in matrix])
# print trans

a = [0,1,2,3,4,5]
del a[0]
print a

del a[2:4]
print a

# 删除列表中全部数据
del a[:]
print a

# 元组 元组在输出时总是有括号的，
# 以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的
t = 12,34,56,"hello"
print t[0]
print t

# 集合
# 如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典
bask = {'a','b','c'}
print 'a' in bask
print 'f' in bask

a = set('abcdefg')
b = set('alal') #集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
print a
print b

print "在a中的字母，但不在b中:",a - b # 在a中的字母，但不在b中
print "在 a 或 b 中的字母:",a | b # 在 a 或 b 中的字母
print "在 a 和 b 中都有的字母:",a & b # 在 a 和 b 中都有的字母
print "在 a 或 b 中的字母，但不同时在 a 和 b 中:",a ^ b # 在 a 或 b 中的字母，但不同时在 a 和 b 中

# 集合推导式
c = {x for x in "abcdefg" if x not in "abc"}
print c

# 字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值
# 构造函数 dict() 直接从键值对元组列表中构建字典

print dict([('aa',11),('bb',22)])

# 字典推导可以用来创建任意键和值的表达式词典
# x**2  x的平方
print {x:x**2 for x in (2,4,6)}

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
tel = {"lisi":20,"zhangsan":21,"wangwu":22}
for x,y in tel.items():
    print x,y

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i,j in enumerate(['11','22','33']):
    print '索引：',i,"值：",j

# 同时遍历两个或更多的序列，可以使用 zip() 组合
q = ['name','age','sex']
a = ['李四',22,'男']
for x,y in zip(q,a):
    print "你的{0}：{1}".format(x,y)
    # print "你的%s：%s" %(q,a)  

# 反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
for i in reversed(range(0,20,2)):
    print i

# 按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
bas = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(bas):
    print i