#!/usr/bin/python
#-*-coding:UTF-8-*-
#Filename:charge2.py

import os
pathFlag = True
while pathFlag:
    # path = raw_input('输入需要监测的文件夹路径: ')
    path = '/Users/admin/Desktop/web/'
    if os.path.exists(path):
        pathFlag = False
    else:
        print '输入的路径不存在'

command = 'cd %s; ls' %path
result = os.popen(command).readlines()

# print ('\n'+ path).join(result)
#1504349364.0  1504349409.0
print path + result[0]
print os.path.getmtime((path + result[0])[:-1])