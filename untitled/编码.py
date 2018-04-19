#coding=utf-8
import sys
if __name__ == "__main__":

    #  当字符串的编码不是utf-8
    print sys.getdefaultencoding( )
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
    print sys.getdefaultencoding( )


    #如果直接执行s.encode('gb2312')
    print "中国".encode('gb2312')