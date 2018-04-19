# -*- coding: utf-8 -*-
# range()函数添加步长参数
# for i in range(1,10,2):
#     print i

# 倒计时
# import time
# for i in range(10,0,-1):
#     print i
#     time.sleep(1)
# print 'OFF'

# 定制乘法表
# 注意输入是字符串，计算时需要转换为int
# num = int(raw_input("which multiplication table would you like?"))
# # for i in range(1,10):
# #     print 5,'*',i,'=',5*i
# maxn = int(raw_input("how high do you want to go?"))
# i = 1
# while i <= maxn:
#     print num,'*',i,'=',num*i
#     i += 1

# ==============可变循环=========
# numblock = int(raw_input("how many blocks of starts do you want?"))
# numline = int(raw_input("how many lines of starts do you want?"))
# num = int(raw_input("how many starts?"))
# for i in range(0,numblock):
#     for j in range(0,numline):
#         for k in range(0,num):
#             print "*",
#         print 
#     print 


# dog_cal = 140
# bun_cal = 120
# ket_cal = 80
# mus_cal = 20
# oni_cal = 40
# print "=======================restart=================="
# print "\tdog \tbun \tketchup\tmustard\tonions\tcalories"
# count = 1
# for dog in[0,1]:
#     for bun in [0,1]:
#         for ket in [0,1]:
#             for mus in [0,1]:
#                 for oni in [0,1]:
#                     total_cal = (dog_cal*dog)+(bun_cal*bun)+\
#                     (ket_cal*ket)+(mus_cal*mus)+(oni_cal*oni)
#                     print "#",count,"\t",
#                     print dog,"\t",bun,"\t",ket,"\t",
#                     print mus,"\t",oni,"\t",
#                     print total_cal
#                     count += 1

import time
tt = int(raw_input("how many seconds?"))
for i in range(tt,0,-1):
    print i,
    for j in range(0,i):
        print "*",
    print
    time.sleep(1)
