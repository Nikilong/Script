#!/usr/bin/python
#coding:utf-8

import time
from selenium import webdriver
#from selenium.webdriver.common.by import By

browser=webdriver.Chrome()

browser.get("http://www.baidu.com")
print(browser.page_source)
#
#input_str = browser.find_element_by_id('kw')
##input_str.send_keys("ipad")
#button = browser.find_element_by_id('su')
#button.click()
#input_str.clear()
#print(input_first)
time.sleep(5)
login_btn=browser.find_element_by_class_name('lb')
#login_btn.click()
login_url=login_btn.get_attribute("href")
browser.get(login_url)

#time.sleep(5)
##网页后退
#browser.back()
#time.sleep(5)
##网页前进
#browser.forward()

#通过执行js脚本'window.open()'来打开一个新的选项
browser.execute_script('window.open()')
#切换到新的选项卡,所有的选项卡都存在window_handles这个数组
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(5)
browser.switch_to_window(browser.window_handles[0])
browser.get('http://www.baidu.com')

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
