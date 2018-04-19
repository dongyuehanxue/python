# -*- coding: utf-8 -*-
import requests
import json

class RunMethod:
	def postMain(self, url, data, headers):
		res = requests.post(url=url, data=data, headers=headers)
		return res.json()
	def getMain(self, url, data, headers):
		res = requests.get(url = url, data = data, headers = headers)
		return res.json()
	def runMain(self, method, url, data = None, headers = None):
		res = None
		if method == 'GET':
			res = self.getMain(url, data, headers)
		else:
			res = self.postMain(url, data, headers)
		return json.loads(json.dumps(res, ensure_ascii=False))

# run = RunMethod()
# res = run.runMain('POST', 'http://hufu.feo.test/api/v2/login', {'username': 'qiaowenyan', 'password': '1'})
# print res

		
