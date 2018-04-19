# -*- coding=utf-8 -*-
# 强制为全局
# my_price = 100
def test():
    # 没有名为my_price的全局变量会创建，有的则会使用
    global my_price
    my_price = 12
    print my_price

test()

class BankAccount(object):
    def __init__(self,username,u_id,num):
        self.username = username
        self.u_id = u_id
        self.num = num
    #显示余额
    def numShow(self):
        return self.num
    # 存钱
    def setNum(self):
        pass
    # 取钱
    def getNum(self):
        pass
class InterestAccount(BankAccount):
    

