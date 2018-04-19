# -*- coding: utf-8 -*-

import sys
# 找到我们自己定义的模块，需要修改sys.path的内容
sys.path.append("D:/GLL/python/quanquan/")
import requests
import json
from runMethod.runMethod import RunMethod
from cases.cases import Cases
        
authorization = ''
class Main:
    def __init__(self):
        self.run_method = RunMethod()
        self.cases = Cases()
    def login(self):
        info = self.cases.getCases()[0]
        res = self.run_method.runMain(info['method'], info['url'], info['data'])
        if 'token' in res:
            print '登陆成功'
        else:
            print '登陆失败'
        self.cases.setAuthorization(res['token'])
    def test(self):
        data = self.cases.getCases()
        successCount = 0
        errorCount = 0
        Total = 0
        print '= 状态 ==== 描述 =============================================================\n'
        for info in data[1:]:
            Total += 1
            res = self.run_method.runMain(info['method'], info['url'], info['data'], info['headers'])
            if info['test'] in res:
                successCount +=1
                print('   √       ' + info['success'])
            else:
                errorCount += 1
                print('   ×       ' + info['fail'])
        print('\n\n======== 测试完毕 ==== 共测试 '+ str(Total) + ' 个接口, 其中成功: '
                + str(successCount) +' 个; 失败: '+ str(errorCount) +' 个 ===========\n\n')
            
run = Main()
run.login()
run.test()
