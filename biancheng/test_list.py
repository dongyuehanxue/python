# -*- coding=utf-8 -*-
list = ['a','b','c','d']
# =========列表分片============
# 分片是愿列表的副本，两者不影响
print list[:]

# ==============向列表添加元素===========
list.append('eee') #向列表末尾添加一个新元素
print list

list.extend(['s','ds','sfds']) #向列表末尾添加多个元素
print list

list.insert(1,'fdffdffd')  #在列表指定位置插入一个元素
print list

# ============从列表删除元素============
list.remove('a')  #从列表删除具体的元素
print list

del list[2]  #使用索引删除元素
print list

dell = list.pop()  #从列表中取出最后一个元素交给你
print 'dell:',dell
print list

list.pop(1)  #可以使用索引
print list 

# =================搜索列表============
# 查找元素是否在列表中  in
if 'd' in list:
    print "found d in list"
else:
    print "did not find d in list"

# 查找索引
if 'd' in list:
    print list.index('d')

# ===============列表排序===============
# sort()对原列表进行排序,没有新建列表
list.sort()
print list
# 逆序排列
# 法1：先正序，再逆置
# list.sort()
# list.reverse()
# print list
# 法2：在sort()中添加属性
list.sort(reverse=True)
print list

# 建立副本列表
# 两者仍指向同一个列表，只不过名字不同
# new_list = list
# print new_list
# new_list.sort()
# print "new_list:",new_list,"list:",list
# 使用分片创建副本,
new_list = list[:]
new_list.sort()
print 'new_list:',new_list,'list:',list

# sorted()得到列表的副本，不影响原列表，进行正序排列
newer = sorted(list)
print newer

# =================双重列表：数据表============
joe = [55,63,77,81]
tom = [65,61,67,72]
beth = [97,95,92,88]
classMarth = [joe,tom,beth]
print classMarth
for i in classMarth:
    print i
# 从双重表中获取一个值
print classMarth[0][2]

# =============练习===========
# print "enter 5 names:"
# names = []
# for i in range(5):
#     names.append(raw_input())
# print "the names are",
# for i in names:
#     print i,
# print 
# # print sorted(names)
# # print 'the third name is ',names[2]
# num = int(raw_input('replace one name.which one?(1-5):'))
# new_name = raw_input('new name:')
# names[num-1] = new_name
# print "the names are",
# for i in names:
#     print i,
# print 

dicts = {}
for i in range(3):
    word_type = raw_input('add or look up a word (a/l)?')
    word = raw_input('type the word:')
    if word_type == 'a':
        word_des = raw_input('type the definition:')
        dicts[word] = word_des
        print 'word add!'
    if word_type == 'l':
        if word in dicts:
            print dicts[word]
        else:
            print 'that word is not in the dictionary yet'