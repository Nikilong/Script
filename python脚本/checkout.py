#!/usr/bin/ env python
# coding:utf-8

import os,time


url = "http://172.20.105.60/svn/exoa_mobile"
path = "/Users/Longcq/Documents/excellence_code/"
while not os.path.exists(path):
    path = raw_input('默认路径不存在,请设置默认路径: ')
print '默认下载路径为:' + path
pathChange = raw_input('是否更改路径: 按下Enter采用默认,否则输入新的路径: ')
if pathChange != "":
    while not os.path.exists(pathChange):
        pathChange = raw_input('输入路径不存在,请输入新路径: ')
    path = pathChange
    print '下载路径成功更改为: ' + path

flag = 0
while flag == 0:
    index = raw_input('checkout代码编号:1.OA  2.WEb壳  3.JS  4.OA打包配置  5.WEB壳打包配置  直接输入代码库地址: ')
    if index == '1':
        url = url + "/iOSClient/branches/SocialOAClient"
        flag = 1
    elif index == '2':
        url = url + "/iOSClient/branches/iExWebClient"
        flag = 1
    elif index == '3':
        url = url + "/iEXJSandOC"
        flag = 1
    elif index == '4':
        url = url + "/ProjectPackage"
        flag = 1
    elif index == '5':
        url = url + "/ProjectPackage/web%e9%a1%b9%e7%9b%ae"
        flag = 1
    else:
        url = index
        if url != "":
            flag = 1

order = 'cd ' + path + ' ;' + 'svn checkout ' + url + ' ;'

if os.system(order):
    print '执行出错'
else:
    print '成功checkout'
    print '代码库地址:' + url
    print '代码下载到路径:' + path


