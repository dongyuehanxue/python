# 打开和关闭文件
# fo = open("11.txt","wb")
# print "文件名：",fo.name
# fo.write("http://www.baidu.com12345678901234567890")

# fo = open("11.txt","r+")
# # read（）方法从一个打开的文件中读取一个字符串
# str = fo.read(20)
# print "从文件中读取：",str
# # 查找当前位置
# pos = fo.tell()
# print "当前位置：",pos

# str1 = fo.read(10)
# print "从文件中读取：",str1

# # 把指针再次重新定位到文件开头
# pos = fo.seek(0,0)
# str2 = fo.read(10)
# print "从文件中读取：",str2


# fo.close()

# Python的os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件

# rename()方法需要两个参数，当前的文件名和新文件名。
# remove()方法删除文件，需要提供要删除的文件名作为参数
import os
# os.rename("11.txt","22.txt")

os.remove("22.txt")