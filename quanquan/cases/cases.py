# -*- coding: utf-8 -*-
class Cases:
	def __init__(self):
		self.authorization = ''
		self.cases = [
			{
				'method': 'POST',
				'url': 'http://hufu.feo.test/api/v2/login',
				'data': {'username': 'qiaowenyan', 'password': '1'},
				'headers': {}
			},
			{
				'method': 'GET',
				'url': 'http://hufu.feo.test/api/v2/users/me',
				'data': {},
				'test': 'username',
				'success': '个人信息获取成功 /users/me',
				'fail': '个人信息获取失败 /users/me',
				'headers': {
					'authorization': self.authorization
				}
			},
			{
				'method': 'GET',
				'url': 'http://hufu.feo.test/api/v2/messages?page=1&size=20&contentType=1&status=1',
				'data': {},
				'test': 'content',
				'success': '消息中心接口访问成功 /messages?page=1&size=20&contentType=1&status=1',
				'fail': '消息中心接口访问失败 /messages?page=1&size=20&contentType=1&status=1',
				'headers': {
					'authorization': self.authorization
				}
			}

		]

	def setAuthorization(self, authorization):
		self.authorization = authorization
		# 全部用例装载 authorization
		for i in self.cases:
			i['headers']['authorization'] = authorization
		return True
	def getCases(self):
		return self.cases

