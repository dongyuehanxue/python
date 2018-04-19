#coding=utf-8
import requests
import json

# ==========  定义请求函数  =====================================================
def request_init(title,url,method):
    headers = {
        'Authorization':token
    }
  
    response = requests.request(method ,URL+url ,headers=headers)
    
    if response.status_code == 200:
        print(title,":OK")
    else:
        print(title,":NG")

    
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
    print("login OK")
else:
    print("login NG")

# ==========  用户接口  =====================================================
print(request_init("用户接口","/api/v2/users/me","GET"))