#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import zipfile,os

def creatSource(name):
    url = "        <url value=\"" + name + "\"/>"

    text2 = '''<?xml version="1.0" encoding="utf-8"?>
        <WebClient>
    	    <version value="1.0.230"/>
    	    <!--
    	    <serverAddress value="http://10.2.6.114:8080"/>
    	    <themeIdentifier value="websource_androidphone"></themeIdentifier>
    	     -->
    	    <LoginUrl>
                <!-- Local 表示资源包内静态页面，Server 表示服务端页面 -->
    		    <type value="Server"/>
        ''' + url + '''
            </LoginUrl>
        </WebClient>
        '''

    f = open("config.xml", "w")

    f.write(text2)

    f.close()

    fz = zipfile.ZipFile('/Users/Longcq/Documents/excellence_code/iExWebClient/iExWebClient/Config/source.zip', 'w',
                         zipfile.ZIP_DEFLATED)
    fz.write("config.xml")
    fz.close()
    os.system('rm -r -f config.xml;')



name = raw_input('请输入地址: 1:Niki.httpServer 2:可输入 3:妇联正式环境 4:工联正式环境 5:街总正式环境 其他情况直接输入网址 ')
if name == '1':
    creatSource('http://172.20.105.87:8000')
    print "替换Niki搭建的测试服务器结束"
#    order = "cp /Users/Longcq/Documents/excellence_file/项目/澳门项目/澳门常用/初始化地址/个人/source.zip /Users/Longcq/Documents/excellence_code/iExWebClient/iExWebClient/Config/source.zip;"
#    if os.system(order) == 0:
#        print "成功替换到：Niki写的放在165的js"
#    else:
#        print "替换niki初始化地址失败"
#-----------
#    zipfile_obj = zipfile.ZipFile('/Users/Longcq/Desktop/test/source.zip', 'w', zipfile.ZIP_DEFLATED)
#    for dirpath, dirnames, filenames in os.walk('/Users/Longcq/Documents/excellence_file/项目/澳门项目/澳门常用/初始化地址/165/source/'):
#        for file in filenames:
#            zipfile_obj.write(file)
#    zipfile_obj.close()
#-----------

elif name == '2':
    order = "cp /Users/Longcq/Documents/excellence_file/项目/澳门项目/澳门常用/初始化地址/ios_输入网址/source.zip /Users/Longcq/Documents/excellence_code/iExWebClient/iExWebClient/Config/source.zip;"
    if os.system(order) == 0:
        print "成功替换到：可自由输入首页地址"
    else:
        print "替换自定义初始化地址失败"
elif name == '3':       # 妇联正式环境
    creatSource('https://app.macauwomen.org.mo/app')
    print "替换妇联正式环境结束"
elif name == '4':       # 工联正式环境
    creatSource('https://app.faom.org.mo/app')
    print "替换工联正式环境结束"
elif name == '5':       # 街总正式环境
    creatSource('https://app.ugamm.org.mo/app')
    print "替换街总正式环境结束"
else:
    creatSource(name)
    print "替换成: " + name

