#coding=utf-8
#xlrd（excel read）来读取Excel文件
import xlrd  
import io

# # 打开Excel文件读取数据
# data = xlrd.open_workbook("11.xlsx")

# # 获取一个工作表
# # table = data.sheets()[0]          #通过索引顺序获取
# # table = data.sheet_by_index(0)    #通过索引顺序获取
# table = data.sheet_by_name(u"Sheet1") #通过名称获取

# # 获取整行和整列的值（数组）
# table.row_values(1)  #行
# table.col_values(1)  #列

# # 获取行数和列数
# nrows = table.nrows 
# ncols = table.ncols

# # 单元格
# cell_a1 = table.cell(0,0).value

# # 使用行列索引
# cell_a1 = table.row(0)[1].value
# cell_a2 = table.col(0)[1].value


# 打来文件
def  open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     
# colnameindex：表头列名所在行的所以  ，by_index：表的索引
# def excel_table_byindex(file= '22.xlsx',colnameindex=0,by_index=0):
#     data = open_excel(file)
#     table = data.sheet_by_index(by_index)
#     nrows = table.nrows #行数
#     ncols = table.ncols #列数

#     colnames = table.row_values(colnameindex) #某一行数据 为获取行里面单元格个数
   
#     list = []
#     for rownum in range(0,nrows):
#         row = table.row_values(rownum)
#         if row:
#             app = {}
#             for i in range(len(colnames)):
#                 app[i] = row[i]
#             list.append(app)
#     return list

# def main():
#     tables = excel_table_byindex()
#     print tables


def excel_table_byindex(file="11.xlsx",colnameindex=0,by_index=0):
    # 调用打开Excel函数打开一个文件
    data = open_excel(file)
    table = data.sheet_by_index(by_index)
    # table = data.sheet()[by_index]

    # 行数
    nrows = table.nrows

    colname = table.row_values(colnameindex)
    # 定义一个空列表，用于存放整个Excel里面的数据
    list = []
    for rownum in range(nrows):
        row = table.row_values(rownum)
        if row:
            # 定义一个空元祖，用于存放一行的数据
            app = {}
            for i in range(len(colname)):
                app[i] = row[i]
            list.append(app)
    return list

# 定义主函数
def main():
    table = excel_table_byindex()
    for i in table:
        print i

# __name__ 是内置变量，用于表示当前模块的名字，同时还能反映一个包的结构
# 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行
if __name__ == "__main__":
    main()