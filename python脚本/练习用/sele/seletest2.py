#!/usr/bin/python
#coding:utf-8

import time
from selenium import webdriver
#from selenium.webdriver.common.by import By

browser=webdriver.Chrome()

login_url="http://moa.fajt.cn:7102/masp/"
browser.get(login_url)
print(browser.page_source)
input_user=browser.find_element_by_id('j_username')
input_user.send_keys('admin')
input_password=browser.find_element_by_id('j_password')
input_password.send_keys('coreadmin')
btn_login=browser.find_element_by_id('loginBtn')
btn_login.click()
print 'login success'
#print browser.page_source
browser.get(login_url+'themeStyle/list.do')


listA=browser.find_elements_by_tag_name('a')
if len(listA) > 0:
    for aEle in listA:
        print 'name:%s  href:%s'%(aEle.text,aEle.get_attribute('href'))
browser.get(listA[0].get_attribute('href'))
print browser.page_source
#
#input_str = browser.find_element_by_id('kw')
##input_str.send_keys("ipad")
#button = browser.find_element_by_id('su')
#button.click()
#input_str.clear()
#print(input_first)
#time.sleep(5)
#login_btn=browser.find_element_by_class_name('lb')
##login_btn.click()
#login_url=login_btn.get_attribute("href")
#browser.get(login_url)
#
#time.sleep(5)
##网页后退
#browser.back()
#time.sleep(5)
##网页前进
#browser.forward()

#执行js脚本
#browser.execute_script('alert("To Bottom")')


#browser = webdriver.Chrome()
#browser.get("http://www.taobao.com")
#print(browser.page_source)
#input_str = browser.find_element_by_id('q')
#input_str.send_keys("ipad")
#time.sleep(50)
#input_str.clear()
#input_str.send_keys("MakBook pro")
#button = browser.find_element_by_class_name('btn-search')
#button.click()

time.sleep(50)
browser.close()
