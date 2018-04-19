# ===============面向对象高级编程====================
# 用MethodType将方法绑定到类，并不是将这个方法直接写到类内部，
# 而是在内存中创建一个link指向外部的方法，在创建实例的时候这个link也会被复制
from types import MethodType
import time
# class Student(object):
#     pass

# 为了达到限制的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class能添加的属性
# class Student(object):
#     __slots__ = ('name','age')


# 使用MethonType给实例绑定一个方法

# 1、把方法绑定到某个类的实例上
# def set_age(self,age):
#     self.age = age

# s1 = Student()
# s2 = Student()
# 实例绑定一个属性
# s.name = 'lulu'
# print s.name

# s1.set_age = MethodType(set_age,s1,Student)
# s1.set_age(11)
# print s1.age
# print s2.age

# 2、将方法绑定在类上（有None参数）。
# 通过该类创建的实例会指向各自不同的区域，各个实例之间互不干扰
# Student.set_age = MethodType(set_age,None,Student)
# s1.set_age(22)
# print s1.age
# s2.set_age(33)
# print s2.age

#3、 将方法绑定在类上（没有None参数）
# 通过该类创建的实例都会指向相同的区域，导致后面实例的值会覆盖前面实例的值

# Student.set_age = MethodType(set_age,Student)
# s1.set_age(44)
# s2.set_age(55)
# print s1.age
# print s2.age


# 定义一个特殊的__slots__变量，来限制该class能添加的属性
# 
# s1.name = 'lulu'
# s1.age = 23
# s1.score = 90

# 使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__

# class ChildStudent(Student):
#     pass

# cs1 = ChildStudent()
# cs1.score = 45
# print cs1.score

# ===================使用@property===============
# class Student(object):
#     # def __init__(self,*score):
#     #     self.__score = score
#     def set_score(self,score):
#         if not isinstance(score,int):
#             # 自定义抛出异常
#             raise ValueError('score 必须是一个整数')
#         if score < 0 or score > 100:
#             raise ValueError('score 必须在0-100之间')
#         self._score = score
#     def get_score(self):
#         return self._score

# s = Student()
# s.set_score(60)
# print s.get_score()


# Python内置的@property装饰器就是负责把一个方法变成属性调用的
# class Student(object):
#     # 把一个getter方法变成属性，只需要加上@property就可以了，
#     # 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self,score):
#         if not isinstance(score,int):
#             raise ValueError('score 必须是整数')
#         if score < 0 or score > 100:
#             raise ValueError('score 必须是0-100内的数')
#         self._score = score

# s = Student()
# s.score = 80
# print s.score
# s.score = 999 #实际转化为s.set_score(999)

# 定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
# class Student(object):
#     @property
#     def birth(self):
#         return self._birth
#     @birth.setter
#     def birth(self,birth):
#         self._birth = birth
#     @property
#     def age(self):
#         # 获取当前时间time.localtime() 年time.localtime().tm_year time.localtime().tm_mon月 time.localtime().tm_mday日
#         return time.localtime().tm_year - self._birth

# s = Student()
# s.birth = 1991
# print(s.age)

# ================多重继承====================
#动物类
# class Animal(object):
#     pass
# #哺乳类和鸟类
# class Mammal(Animal):
#     pass
# class Bird(Animal):
#     pass

# #定义功能类
# class Runnable(object):
#     def run(self):
#         print 'running...'

# class Flyable(object):
#     def fly(self):
#         print 'flying...'

# #各种动物
# # 对于需要Runnable功能的动物，就多继承一个Runnable
# class Dog(Mammal,Runnable):
#     pass
# class Bat(Mammal,Flyable):
#     pass
# class Parrot(Bird):
#     pass

# d1 = Dog()
# d1.run()

# Mixin的目的就是给一个类增加多个功能，
# 这样，在设计类的时候，我们优先考虑通过多重继承来组合多个Mixin的功能，
# 而不是设计多层次的复杂的继承关系

#=================定制类================
# 定义好__str__()方法，返回一个好看的字符串
#    
# class Student(object):
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name:%s)' % self.name
#     __repr__ = __str__

# print(Student('李四'))

# 直接显示变量调用的不是__str__()，而是__repr__()
# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
# 也就是说，__repr__()是为调试服务的。

# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环

# 以斐波那契数列为例
# class Fib(object):
#     def __init__(self):
#         self.a,self.b = 0,1
#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己
#     def next(self):
#         self.a,self.b = self.b,self.a+self.b
#         if self.a > 1000:
#             raise StopIteration
#         return self.a #返回下一个值

# for n in Fib():
#     print n

# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行
# print Fib()[2]

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
# class Fib(object):
#     def __getitem__(self,n):
#         a,b = 0,1
#         for x in range(n):
#             a,b = b,a+b
#         return a

# f = Fib()
# print f[0]


# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样
class Student():
    def __init__(self,name):
        self.__name = name
    def __call__(self,tt):
        print('name is %s,%s' % (self.__name,tt))

s = Student('lulu')
print s('434')

# __getattr__()方法，动态返回一个属性
# class Student(object):
#     def __init__(self,path=''):
#         self.__path = path
#     def __getattr__(self,path):
#         return Student('%s/%s' % (self.__path,path))
#     def __str__(self):
#         return self.__path

# print Student().status.meth
# 解析：Student()中没有status属性，调用__getattr__方法，返回Student('/status')
# Student('/status').meth 中没有meth属性，调用__getattr__方法，返回Student('/status/method')
# 最后执行__str__

# Chain().users('michael').repos
class China(object):
    def __init__(self,path=''):
        self.__path = path
    def __getattr__(self,path):
        return China('%s/%s' % (self.__path,path))
    def __str__(self):
        return self.__path
    __repr__ = __str__
    __call__ = __getattr__

print China().users('zhangshan')
# 解析：China().users china中没有user属性，调用__getattr__，返回china('/users')
# china('/users')('zhangshan')  将对象看做一个函数，直接调用，__call__方法，可以传参
# __call__方法与__getattr__方法一样，返回china('/user/zhangsan')


# ==============枚举类=========================
from enum import Enum
Month = Enum('Weekday',('Mondy','Tuesday','Wednesday','Thursday','Firday','Saturday','Sunday'))
for name, member in Month.__members__.items():
    print(name, '=>', member.value)

print Month.Mondy
# 
# value属性则是自动赋给成员的int常量，默认从1开始计数
print Month['Tuesday'].value