#coding=utf-8
# -*- coding: UTF-8 -*-

import time
ticks = time.time()
# print("当前时间戳：",ticks)  python3以后使用
print "当前时间戳：",ticks

# 获取当前时间
localtime = time.localtime(time.time()) #time.localtime(time.time()) == time.localtime()
# print "本地时间：",localtime
print time.localtime()


"""
获取格式化的时间
1、最简单的获取可读的时间模式的函数是asctime():

格式化日期
使用 time 模块的 strftime 方法  time.strftime(format[, t])
"""
localtime2 = time.asctime(localtime)
print "格式化后的本地时间：",localtime2

print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

print time.strftime("%Y %b %d %a %H:%M:%S",time.localtime())


# 将格式字符串转换为时间戳
a = "2018 Jan 05 Fri 15:27:31"
print time.mktime(time.strptime(a,"%Y %b %d %a %H:%M:%S"))


# 获取某月日历   import calendar

import calendar
cal = calendar.month(2017,12)
print "输出2017.12月日历："
print cal

print calendar.month(2018,1)

# 是闰年返回True，否则为false
print calendar.isleap(2018)

# 返回在Y1，Y2两年之间的闰年总数
print calendar.leapdays(2000,2018)

