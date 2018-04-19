# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式
f = abs
print f(-10)
def add(x,y,f):
    return f(x)+f(y)

print(add(5,-4,abs))


# Python内建了map()和reduce()函数。
# map()函数接收两个参数，一个是函数，一个是序列，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回

# 比如我们有一个函数f(x)=x*x，
# 要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现
def f(x):
    return x*x

print(map(f,[1,2,3,4,5,6,7,8,9,10]))

# 讲list中数字转为字符
print(map(str,[1,2,3,4,5]))

# reduce把一个函数作用在一个序列[x1, x2, x3...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 对一个序列求和  sum()函数
def add(x,y):
    return x+y

print 'sum:',reduce(add,[1,2,3,4,5])

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

def change(x):
    x = x.lower()
    x = x[0].upper()+x[1:]
    return x

print(map(change,['adam','LISA','barT']))

# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
    return x*10+y

print(reduce(fn,[1,3,5,7,9]))


# 把str转换为int的函数
# map()返回一个新的list reduce把结果继续和序列的下一个元素做累积计算

def fn(x,y):
    return x*10+y

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

# 字符串str也是一个序列
print('str to num:',reduce(fn,map(char2num,'13579')))

# 整合成str2int函数
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(char2num,s))

print(str2int('123'))


# 求积
def prod(x,y):
    return x*y

print(reduce(prod,[1,2,3,4,5]))

# filter()函数用于过滤序列
# 和map()类似，filter()也接收一个函数和一个序列
# 和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n%2 == 1

print(filter(is_odd,[1,2,3,4,5,6,7,8,9]))


# 用filter()删除1~100的素数：
def is_prime(n):
    if n == 1:
        return True
    for i in range(2,n):
        if n % i == 0:
            return True
        return False
# ==========列表推导式===========
print(filter(is_prime,[x for x in range(1,100)]))

# sorted()函数就可以对list进行排序
l = [0,2,-1,33,45,12]
print(sorted(l))

s = ['bob', 'about', 'Zoo', 'Credit','aa']
print(sorted(s))

# 排序应该忽略大小写，按照字母序排序
def cmp_ignore_case(s1,s2):
    s1 = s1.upper()
    s2 = s2.upper()
    if s1 < s2:
        return -1
    if s1 == s2:
        return 0
    if s1 > s2:
        return 1

s = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(s,cmp_ignore_case))

# ===========函数作为返回值==============
def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum

d = lazy_sum(1,2,3,4)
# 返回的并不是求和结果，而是求和函数
print(d)
print(d())

# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1,2,3,4)
f2 = lazy_sum(1,2,3,4)
print(f1==f2)

# 返回的函数并没有立刻执行，而是直到调用了f()才执行
# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i * i
#         fs.append(f)
#     return fs
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

a1 = count()
# 返回的函数引用了变量i，但它并非立刻执行。 
# 以函数形式存在fs列表中，[i*i,i*i,i*i] 当调用f()时，i已经变成了3
# 等到3个函数都返回时，它们所引用的变量i已经变成了3

print [x() for x in a1]

# 闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
    fs = []
    for i in range(1,4):
        def f(j):
            return j*j
        fs.append(f(i))
    return fs

a1 = count()
print(a1)

# ==========匿名函数 lambda==========
f = lambda x:x*x
print(f(5))

# 函数对象有一个__name__属性，可以拿到函数的名字
print f.__name__

# ==========装饰器（Decorator）===========
# 增强now()函数的功能
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式
# decorator就是一个返回函数的高阶函数
import time
# 接受一个函数作为参数，并返回一个函数
def log(func):
    def wrapper(*args,**kw):
        print 'call %s():' %func.__name__
        return func(*args,**kw)
    return wrapper

# 需要把原始函数的__name__等属性复制到wrapper()函数中
# ,否则，有些依赖函数签名的代码执行就会出错,Python内置的functools.wraps就是干这个事的
import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print 'call %s' % func.__name__
#         return func(*args,**kw)
#     return wrapper

# 带参数的decorator
def log(*text):
    def decorator(func):
        def wrapper(*args,**kw):
            print '%s call %s' % (text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

# 借助Python的@语法，把decorator置于函数的定义处
# @log
@log('text')
def now():
    print time.asctime(time.localtime())

print now()
print now.__name__


# ============偏函数=============
# int()函数可以把字符串转换为整数
print int('123456')
# int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
print int('10101',base=2)  

# functools.partial就是帮助我们创建一个偏函数的
int2 = functools.partial(int,base=2)

print int2('10101')

# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
print int2('1212',base=8)

max2 = functools.partial(max,10)

print max2(1,2,3,4,5,11)
print max2(range(10)) #相当于max(10,range(10))比较10<range(10)
print 10>range(10)
print max(range(10))