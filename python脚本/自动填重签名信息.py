#!/usr/bin/python
#coding:UTF-8

import os,re,sys,time,urllib
from selenium import webdriver
from selenium.webdriver.support.ui import Select

print '''
==========================使用说明==========================
第1个参数是ipa包上传路径,第2个参数是bundle id,第3个参数是下拉签名证书(输入顺序号),第4个参数是mobileprovision文件路径
'''

def  fillInputWithId(browser, id, string):
    input = browser.find_element_by_id(id)
    input.clear()
    if input:
        input.send_keys(string)

print '需要重签的ipa包是:%s'%sys.argv[1]
version = re.findall('1\.\d+\.\d+',sys.argv[1])[0]
version = '%s%s'%(version[:-1],(int(version[-1]) + 1))

browser = webdriver.Chrome()
browser.get('http://172.20.105.89:8090/SSH/manage!toResignPage.do')
# 等待网页加载完成
time.sleep(5)
#记录操作,最后统一输出
record = '\n---->Operation Record:\n###start operation###\n'

#bundleTd
if len(sys.argv) > 2:
    fillInputWithId(browser, 'bundleId',sys.argv[2])
    record = '%s{input bundle_id:%s}---'%(record,sys.argv[2])
#fillInputWithId(browser, 'appName','')     #app名称
#版本号
fillInputWithId(browser, 'appVersion',version)
record = '%s{input app_version:%s}---'%(record,version)

input_whiteList_list = browser.find_elements_by_id('whiteList')
for ele in input_whiteList_list:
    if  ele.get_attribute('value') in ('KingsoftOfficeApp','iCAB','iCABHD'):
        ele.click()
        record = '%s{check whiteList:%s}---'%(record,ele.get_attribute('value'))

#下拉框,signCertificate
#先定位到下拉框
sele_signCertificate_list = browser.find_element_by_id('signCertificate')
if len(sys.argv) > 3:
    Select(sele_signCertificate_list).select_by_index(sys.argv[3])
    record = '%s{select signCertificate at index:%s(default 2)}---'%(record,sys.argv[3])
else:
    Select(sele_signCertificate_list).select_by_value('Excellence Information Technology Corp., Ltd.')
    record = '%s{select default signCertificate:\'Excellence Information Technology Corp., Ltd.\'}---'%record

#文件上传
sele_fileInput_list = browser.find_elements_by_id('file')
#mobileprovision
if len(sys.argv) > 4:
    sele_fileInput_list[1].send_keys(sys.argv[4])
    record = '%s{upload mobileprovision:%s}---'%(record,sys.argv[4])
#ipa上传
sele_fileInput_list[0].send_keys(sys.argv[1])
record = '%s{upload ipa:%s}------\n###end operation###'%(record,sys.argv[1])

print record
ss = input('\n请确认重签配置是否正常,输入任意按钮继续,输入enter退出程序')
# 直接执行按钮的时间以便页面跳转
browser.execute_script('javascript:{this.disabled=true;document.packageForm.submit();}')
print '---->开始重签.......'
time.sleep(5)
downloadUrl = browser.find_element_by_id('downloadUrl').get_attribute('href')
print '---->get client url: %s'%downloadUrl
save_path = '%s%s.ipa'%(sys.argv[1][:-5],(int(sys.argv[1][-5]) + 1))
file = urllib.urlopen(downloadUrl)
with open(save_path, 'wb') as f:
    f.write(file.read())

print '重签后文件保持到: %s'%save_path
time.sleep(200)
browser.close()

