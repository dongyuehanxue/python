#-*- coding=utf-8 -*-
# 使用from导入模块，函数会包含到主程序的命名空间中
# 随机数模块
import random
import time
# 随机整数
print random.randint(0,100)
# 随机小数
print random.random()*10

# ==========练习==============
listNum = []
for i in range(5):
    x = random.randint(1,21)
    listNum.append(x)
print listNum

for i in range(30):
    time.sleep(1)
    i += 1
    if i%3 == 0:
        print random.random()*10
print "time done"