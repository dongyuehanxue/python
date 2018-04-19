# class后面紧接着是类名，即Student，类名通常是大写开头的单词,紧接着是(object)，表示该类是从哪个类继承下来的
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

# ============类和实例=================
class Student(object):
    # def __init__(self,name,score):
    #     self.name = name
    #     self.score = score

    # def print_score(self):
    #     print '%s:%s' %(self.name,self.score)

    # def get_score(self):
    #     if self.score > 90:
    #         print 'A'
    #     elif self.score > 80:
    #         print 'B'
    #     else:
    #         print 'C'
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print '%s:%s' %(self.__name,self.__score)
    def get_score(self):
        return self.__score
    def set_score(self,score):
        self.__score = score

    

# student = {'张三':20,'李四':85,'王五':40}
# for i in student:
#     one = Student(i,student[i])
#     one.print_score()
#     # one.get_score()

two = Student('赵丽',96)
two.set_score(80)
print(two.get_score())

# 判断一个变量是否是某个类型可以用isinstance()判断
print(isinstance(two,Student))

# ==============继承和多态==============
class Animal(object):
    def run(self):
        print 'Animal is running....'

class Dog(Animal):
    # pass
    def run(self):
        print 'dog is running...'

class Cat(Animal):
    # pass
    def run(self):
        print 'dog is running...'
class Mi(Animal):
    def run(self):
        print 'Mi is running slowly...'

def run_write(animal):
    animal.run()


# dog = Dog()
# print(dog.run())

# run_write(Animal())
# run_write(Dog())
# run_write(Mi())

class Animal2(object):
    def run(self):
        print 'Animal is running..'

class People(object):
    def run(self):
        print 'People is running...'
class Man(People,Animal2):
    pass

# Man类按照这样的继承顺序来写。
# 因为python新式类的继承用了新的MRO方法，处理多重继承的时候，继承的属性、方法等是按照（P1，P2）从左往右搜索的，
# 比如说run()，如果在P1中搜索到了此方法，那么子类Man的run()就会调用P1的
mi = Man()
mi.run()
# super(Animal2,Man()).run()


# ================获取对象信息=============
# 对象类型，使用type()函数
print(type(123)==type(456))
print(type(123)==type('123'))

import types
print(type('1234') == types.StringType)
print(type(u'abc') == types.UnicodeType)
print(type([]) == types.ListType)
print(type(int) == type(str) == types.TypeType)

# 获得一个对象的所有属性和方法,使用dir()
print(dir('AB'))

