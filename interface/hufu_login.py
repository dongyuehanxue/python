
#coding=utf-8
import requests
# 编码和解码JSON数据
import json 

# 虎符登录  从服务器获取token
url ="http://hufu.feo.test"
uname = "genglulu"
pwd = "1"

payload = "username="+uname+"&password="+pwd
headers = {
    # Content-Type说明了请求主体的内容是如何编码的,针对简单URL编码的MIME类型
    'Content-Type': "application/x-www-form-urlencoded"
    
    }

response = requests.request("POST", url+"/api/v2/login", data=payload, headers=headers)
# json.dump() 和 json.load() 来编码和解码JSON数据
token = json.loads(response.text)["token"]
print(token)

# print(response.status_code)

if response.status_code == 200:
    print("OK")
else:
    print("NG")
print("\n\n\n")

# 虎符获取当前用户信息
# url = "http://hufu.feo.test/api/v2/users/me"

headers = {
    'Authorization': token
    }

response = requests.request("GET", url+"/api/v2/users/me", headers=headers)

print(response.text)
