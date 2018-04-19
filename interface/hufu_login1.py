#coding=utf-8
import requests
import json

# ==========  全局基础设置  =====================================================
# 全局token
token = ""
URL = "http://hufu.feo.test"
uname = "genglulu"
pwd = "1"

# ==========  登录接口  =====================================================
paylod = "username="+uname+"&password="+pwd
headers = {
    'Content-Type': "application/x-www-form-urlencoded"
}

response = requests.request("POST",URL+"/api/v2/login",data=paylod,headers=headers)

if response.status_code == 200:
    token = json.loads(response.text)["token"]
    print("OK")
else:
    print("NG")

# ==========  用户接口  =====================================================
headers = {
    'Authorization': token
}
response = requests.request("GET" ,URL+"/api/v2/users/me", headers=headers)
if response.status_code == 200:
    print("OK")
else:
    print("NG")
