#coding=utf-8
# from selenium import webdriver
# import time

# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# elem = driver.find_element_by_id("kw")
# elem.clear()
# elem.send_keys("python")

# btn = driver.find_element_by_id("su")
# btn.click()

# time.sleep(5)
# driver.close()

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://hufu.feo.test/login")
user = driver.find_element_by_name("loginName")
pwd = driver.find_element_by_name("password")
btn = driver.find_element_by_xpath(".//*[@id='app']/div/form/div[3]/div/button")

userList = [" ","hh","genglulu","@##@!!#DF#E12"]
pwdList = [" ","kk","1","@##@!!#DF#E12"]

# 测试登录
for i in userList:
    for j in pwdList:
        time.sleep(2)
        user.clear()
        pwd.clear()
        user.send_keys(i)
        pwd.send_keys(j)
        btn.click()
        if driver.current_url == "http://hufu.feo.test/layout/dashboard":
            print "pass"
        else:
            print "NG"

# 点击进入策略
strange = driver.find_element_by_xpath(".//*[@id='app']/section/section/aside/ul/li[2]")






