#!/usr/bin/env python
#coding:utf-8

import os

path = raw_input("请输入ipa包或者Mobileprovision的路径: ")
# path = '/Users/Longcq/Desktop/test/JF_CUSTOMER_iExClient-svn38947-1.0.1443.ipa'

if '.ipa' in path:
    order = 'unzip ' + path + ' ;'
    os.popen(order).readline()
    ipaName = os.popen('ls Payload').readlines()[0][0:-1]
    order2 = 'security cms -D -i Payload/' + ipaName + '/embedded.mobileprovision ;' + 'rm -r Payload/ ;'
elif '.mobileprovision' in path:
    order2 = 'security cms -D -i ' + path + ' ;'
os.system(order2)
print '\n' + path

