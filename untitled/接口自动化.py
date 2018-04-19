# -*- coding: utf-8 -*- 
# def function(str):
#     a = 2
#     b=3
#     c=5
#     d = a + b
#     print d == c
#     print str
#     print str
#     print str
#     print str
#     print str
#     print str
#     print str

# function("我是罗圈圈")


baseUrl = "https://mp.luoquanquan.com/api/v1/"
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = baseUrl + "users/home"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, verify=False)

print(response.ok)


# /users/me/{examTypeId}

url = baseUrl + "/users/me/1234?examTypeId=1234"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, verify=False)

print(response.ok)