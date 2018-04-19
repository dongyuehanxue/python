#coding = utf-8
# while True:
#     try:
#         x = 10 / 0
#         break
#     except (ValueError,NameError,TypeError,ZeroDivisionError):
#         print "异常"

# def this_fails():
#     x = 1/10

# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print "错误",err

# 抛出异常
# Python 使用 raise 语句抛出一个指定的异常
# try:
#     raise NameError("error")
# except NameError:
#     print '异常'
#     raise


# def divide(x,y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print "被除数不能为0"
#     else:
#         print "result:",result
#     finally:
#         print "都执行"

# divide(2,0)
# divide(4,2)

# 预定义的清理行为
# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
# python中的with语句使用于对资源进行访问的场合，保证不管处理过程中是否发生错误或者异常都会执行规定的__exit__（“清理”）操作，释放被访问的资源，比如有文件读写后自动关闭、线程中锁的自动获取和释放等。
# with open("22.txt") as f:
#     for i in f:
#         print i
#     f.read()


# 记录错误
# 出错后，程序打印完错误信息后会继续执行
import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except StandardError,e:
        logging.exception(e)
main()
print 'END'