#coding=utf-8
import requests
import json
import xlrd
from xlutils.copy import copy

# ==========  定义请求函数  =====================================================
def requests_init(method,url,param,headers,x,y):
    if method == "POST":
        request = requests.request(method,URL+url,headers=headers,data=param)
    if method == "GET":
        request = requests.request(method,URL+url,headers=headers,params=param)
    if request.status_code == 200:
        print 'OK'
        ws.write(x,y,"OK")
    else:
        print 'NG'
        ws.write(x,y,"NG")
    wd.save("IO.xls")
    return request

# ==========  定义全局变量  =====================================================
URL = "http://hufu.feo.test"
token = ""

# ==========  打开文件  =====================================================
workbook = xlrd.open_workbook("IO.xls")
table = workbook.sheet_by_index(0)
wd = copy(workbook)
ws = wd.get_sheet(0)
nrow = table.nrows

# ==========  主函数  =====================================================
def main():
    for i in range(1,nrow):
        if table.cell(i,1).value == "/api/v2/login":
            header = {"Content-type":"application/x-www-form-urlencoded"}
            rs = requests_init(table.cell(i,0).value,table.cell(i,1).value,table.cell(i,2).value,header,i,4)
            token = json.loads(rs.text)["token"]
        else:
            header = {"Authorization":token}
            requests_init(table.cell(i,0).value,table.cell(i,1).value, table.cell(i,2).value ,header,i,4)
    
if __name__ == "__main__":
    main()

    




