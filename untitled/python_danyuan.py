#-*- coding:utf-8 -*-
# 单元测试 使用python自带的unittest
# 编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问
class Dict(dict):
    def __init__(self,**kw):
        # super() 函数是用于调用父类(超类)的一个方法
        # super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
        # 但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
        super(Dict,self).__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self,key,value):
        self[key] = value

# 引入unittest
import unittest
# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承
class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1,b='test')
        # 最常用的断言就是assertEquals()
        self.assertEquals(d.a,1)
        self.assertEquals(d.b,'test')
        # 测试该表达式是真值（或假值） assertTrue/assertFalse
        # isinstance(object, classinfo)是python内置函数，判断参数object是不是classinfo的实例
        self.assertTrue(isinstance(d,dict))
    
    # 测试使用对象.方法访问值
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key,'value')
    
    # 测试使用属性访问值
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'],'value')
    # 另一种重要的断言就是期待抛出指定类型的Error  assertRsise
    # python中的with语句使用于对资源进行访问的场合，保证不管处理过程中是否发生错误或者异常都会执行规定的__exit__（“清理”）操作，
    # 释放被访问的资源，比如有文件读写后自动关闭、线程中锁的自动获取和释放等。
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['emem']
    
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.emem

    # 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。
    # 这两个方法会分别在每调用一个测试方法的前后分别被执行
    def setUp(self):
        print 'start,,,,,,'

    def tearDown(self):
        print 'end.........'
# 运行单元测试时，1、添加主函数 可以当做正常的脚本执行
if __name__ == '__main__':
    unittest.main()
# 2、在命令行中通过参数python -m unittest python_error2运行,推荐使用此方法，可以批量运行多个单元测试

