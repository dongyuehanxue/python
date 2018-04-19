#encoding=utf-8
import xlrd
from xlutils.copy import copy

workbook = xlrd.open_workbook("tt.xls")
sheet = workbook.sheet_by_index(0)
wb = copy(workbook)

#通过get_sheet()获取的sheet有write()方法
ws = wb.get_sheet(0)
ws.write(5,1,"三生三世222".decode("utf-8"))
ws.write(5,1,"三生三世444".decode("utf-8"))
wb.save("tt.xls")