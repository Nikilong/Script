#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#Filename:chargeTheFile.py

#定时遍历文件夹检测文件数量的改变
import os, time

redStr = '\033[31m'
greenStr = '\033[32m'
yellowStr = '\033[33m'
clearColorStr = '\033[0m'

#遍历文件夹
def Traversal(path):
    filelist = []
    mtime = {}
    # print filelist
    for root, dirs, files in os.walk(path):
        for filespath in files:
                if '.DS_Store' in filespath:
                    continue
                file = os.path.join(root, filespath)
                filelist.append(file)
                mtime[file] = os.path.getmtime(file)  #将每个文件的修改时间存为字典,拼接到数组最后面
    filelist.append(mtime)
    return filelist

# fileFlag = True
# while fileFlag:
#     path = raw_input('输入需要检测的文件夹路径: ')
#     if os.path.exists(path):
#         fileFlag = False
#     else:
#         print redStr + '输入的文件夹路径不存在' + clearColorStr

path = '/Users/admin/Desktop/web'
originList = Traversal(path)
# print originList[-1]
# print set(originList[-1].items())

# 监测新旧文件夹状态
def check():
    newList = Traversal(path)
    addArr = set(newList[:-1]).difference(set(originList[:-1]))  # 增加了文件
    reduceArr = set(originList[:-1]).difference(set(newList[:-1]))  # 删除了文件
    originMtimeDict = originList[-1]
    newMtimeDict = newList[-1]
    isChange = False
    for keyO in originMtimeDict:  # 对比两个字典是否不同
        for keyN in newMtimeDict:
            if keyN == keyO:
                if originMtimeDict[keyO] != newMtimeDict[keyN]:
                    flat = False
                    isChange = True
                    print yellowStr + ' modify : ' + keyN + clearColorStr
    if len(addArr):
        flat = False
        isChange = True
        print greenStr + ' add : ' + '\n add : '.join(addArr) + clearColorStr
    if len(reduceArr):
        flat = False
        isChange = True
        print redStr + ' delete : ' + '\n delete : '.join(reduceArr) + clearColorStr
    if isChange == False:
        print 'no change'

def nextToDo():
    print 'next to do something'

def star():
    while True:
        cmd = int(raw_input('接下来的指令是: (1:监测文件夹状态  2:检测文件夹文件状态  3:退出 ) : '))
        if cmd == 1:
            print '正在监测该文件夹的修改情况......'

            flat = True
            index = 0
            duration = 10  # 进行一次检测的时间间隔
            while flat:
                index += duration
                if index >= 60:
                    print redStr + 'out of time' + clearColorStr
                    break
                time.sleep(duration)
                check()
        elif cmd == 2:
            check()
        elif cmd == 3:
            break
        elif cmd == 4:
            nextToDo()
        else:
            print '无效指令'
