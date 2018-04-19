#coding=utf-8
# num = [2,3,4,5,6,7]
# even = []
# odd = []
# # while 循环，条件成立循环
# while len(num) > 0:
#     number = num.pop()
#     if(number % 2 == 0):
#         even.append(number)
#     else:
#         odd.append(number)
#
# count = 0
# while(count < 10):
#     if (count % 2 == 0):
#         print 'count is',count
#     count = count + 1

"""continue  break"""
# i = 1
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print i

# 此外"判断条件"还可以是个常值，表示循环必定成立
# i = 1
# while 1: # 循环条件为1必定成立
#     print i
#     i += 1
#     if i > 10:
#         break

"""while … else 在循环条件为 false 时执行 else 语句块"""
num = 1
while num < 10:
    print(num,'小于10')
    num += 1
else:
    print(num,'不小于10')

"""
range()函数，可以生成一个整数序列,从0开始
通过list()函数可以转换为list
"""
num = list(range(101))
# print(num)
# sum = 0
# for i in range(101):
#     sum = sum + i
# print(sum)

# for i in num:
#     if i/10 < i%10:
#         print(i)

# 多重循环
for i in ['1','2','3']:
    for j in ['1','2','3']:
        print(i+j)




