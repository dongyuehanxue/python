import http.client
import json

# ==========  全局基础设置  =====================================================
# 定义全局 token
token = ''

conn1 = http.client.HTTPConnection("hufu.feo.test")

# ==========  登陆接口  ========================================================
payload = "username=genglulu&password=1"
# payload = "username=qiaowenyan&password=1"

# 请求信息
headers = {
    'content-type': "application/x-www-form-urlencoded"
    }
# 请求发送
conn1.request("POST", "/api/v2/login", payload, headers)

# 响应解析
res1 = conn1.getresponse()
data = res1.read()
if res1.status == 200:
    print('登陆接口正常')
    token = json.loads(data.decode("utf-8"))['token']
else:
    print('登陆失败')  

# ==========  me 接口, 获取个人信息  ============================================
conn2 = http.client.HTTPConnection("hufu.feo.test")
headers = {
    'content-type': "application/json",
    'authorization': token,
    }
conn2.request("GET", "/api/v2/users/me", headers=headers)
res2 = conn2.getresponse()
if res2.status == 200:
    print('获取个人信息接口返回成功')
else:
    print('获取个人信息接口返回失败')

# ==========  获取策略列表接口, 用于 sop 工作台审批管理展示条目  ==================
conn3 = http.client.HTTPConnection("hufu.feo.test")
headers = {
    'content-type': "application/json",
    'authorization': token,
    }
conn3.request("GET", "/api/v2/strategies?status=&pageSize=3&auditStatus=0&pageNum=1&area=&own=&orgs=&firstProjectId=", headers=headers)
res3 = conn3.getresponse()
if res3.status == 200:
    print('sop 工作台审批管理展示条目, 加载成功')
else:
    print('sop 工作台审批管理展示条目, 加载失败')



# ==========  工作台录音列表  ===================================================
conn4 = http.client.HTTPConnection("hufu.feo.test")

headers = {
    'content-type': "application/json",
    'authorization': token,
    }
conn4.request("GET", "/api/v2/calls?%3Fpage=1&size=5&enterpriseId=&groupId=&sellId=&sellGroupId=&workNum=&state=&recordType=&recType=&isApply=&isSystem=&startTimeLength=0&endTimeLength=0&selectStatus=", headers=headers)
res = conn4.getresponse()
if res.status == 200:
    print('sop 工作台录音列表, 加载成功')
else:
    print('sop 工作台录音列表, 加载失败')


