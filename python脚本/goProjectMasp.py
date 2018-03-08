#!/usr/bin/python
#coding:utf-8

import os,sys,re,webbrowser,urllib


def dealXml(path):
    with open(path,'r') as f:
        for line in f.readlines():
            if 'serverAddress' in line:
                return line
    return none

path='%s/iOS/'%sys.argv[1]
#serverAddress_list=[]
#serverAddress_str=''
if os.path.exists(path):
    path=path + '/initConfig.xml'
    os.system('cat \'%s\''%path)
    serverAddress_str=dealXml(path)
    url_list=re.findall('\"http.*?\"',serverAddress_str)


    if len(url_list)>0:
        url=url_list[0][1:-1]
        print '提取到初始化地址为:'+url
#        webbrowser.open('%s/masp/app/applist.jsp'%(url))
        webbrowser.open('%s/masp/app'%(url))
        webbrowser.open('%s/masp'%(url))
    
    else:
        print '\n该项目iOS打包配置初始化地址为空'
else:
    print '该项目没有iOS的打包配置'

print '当前处理文件夹是: '+sys.argv[1]

