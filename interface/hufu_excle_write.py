# 使用xlwt（excel write）来生成Excel文件
# 对于已经存在的Excel文件进行修改
# 使用xlutils（依赖于xlrd和xlwt）提供复制excel文件内容和修改文件的功能
# -*- coding: utf-8-*-
import xlwt
import io

# # 创建工作簿和工作页
# # wookbook = xlwt.Workbook()
# #指定以utf-8的格式打开
# wookbook =xlwt.Workbook(encoding = 'utf-8')
# #指定打开的sheet页
# sheet = wookbook.add_sheet("Sheet1")

# # 写入单元格
# sheet.write(0,0,'中文') #行，列，值
# #保存
# wookbook.save("tt.xls")


# 样式
def style():
    style = xlwt.XFStyle()  #初始化样式
    font = xlwt.Font()    #为样式创建字体
    font.name = 'Times New Roman'
    font.bold = True
    font.colour_index = 4
    font.height = 220
    return style

workbook = xlwt.Workbook(encoding = 'utf-8')
sheet = workbook.add_sheet("demo")
row0 = ["ID","姓名","年龄","性别"]




# 表头信息
for i in range(len(row0)):
    #  excle中中文显示：row0[i].decode("utf-8")
    sheet.write(0,i,row0[i],style())

data={'1':['张三','20','男'],'2':['李四','21','女'],'3':['王五','22','女']}
ldata = []
#for循环指定取出key值存入num中
num = [a for a in data]
# num.sort
# print(num)
#for循环将data字典中的键和值分批的保存在ldata中
# 将data字典中的值转换为列表存储
for x in num:
    t = [x]
    for a in data[x]:
        # 依次添加到列表里面
        t.append(a)
    ldata.append(t)
# print(ldata)

# enumerate函数用于遍历序列中的元素以及它们的下标,多用于在for循环中得到计数
for i,j in enumerate(ldata):
    for x,y in enumerate(j):
        print i,x,y
        sheet.write(i+1,x,y)

workbook.save("tt.xls")