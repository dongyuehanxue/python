# -*- coding: utf-8 -*-
# GUI 图形用户界面
import easygui
# msgbox用于创建一个消息框
# user_res = easygui.msgbox("hello!")
# print user_res

# ===========对话框 buttonbox
# fla = easygui.buttonbox('choice',choices=['11','22','33'])
# easygui.msgbox('choice:'+fla)

#=========== 选择框 choicebox
# fla = easygui.choicebox('your choice',choices=['11','22','33'])
# easygui.msgbox('choice:'+fla)

# ===========输入框 enterbox
# flag = easygui.enterbox('your name') 
# 带有默认值的输入
flag = easygui.enterbox('your name',default='lili')
easygui.msgbox('name:'+flag)

# ==========整数框 integerbox  
