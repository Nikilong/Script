#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#FileName:webAppPackage.py

import os
import time

pro = raw_input('project name(fl:妇联,gl:工联): ')

pathSource = '/Users/Longcq/Documents/excellence_code/web上架/'
pathDen = '/Users/Longcq/Documents/excellence_code/iExWebClient/iExWebClient'
if pro == 'fl':
    pathSource = pathSource + 'am_澳门web项目婦女聯合總會'
elif pro == 'gl':
    pathSource = pathSource + 'am_澳门web项目工會聯合總會'


order = '''
    cp %s/Icon-72.png %s/icons/Icon-72.png ;
    cp %s/Icon-72\@2x.png %s/icons/Icon-72\@2x.png ;
    cp %s/Icon-72\@3x.png %s/icons/Icon-72\@3x.png ;
    cp %s/Icon-76.png %s/icons/Icon-76.png ;
    cp %s/Icon-76\@2x.png %s/icons/Icon-76\@2x.png ;
    cp %s/Icon-120.png %s/icons/Icon-120.png ;
    cp %s/Icon-Small.png %s/icons/Icon-Small.png ;
    cp %s/Icon-Small-50.png %s/icons/Icon-Small-50.png ;
    cp %s/iTunesArtwork %s/icons/iTunesArtwork ;
    
    cp %s/source.zip %s/Config/source.zip ;
    cp %s/PackageDefine.h %s/Networks/EXGetDataLib/publicDefine/PackageDefine.h ;
    cp %s/Info.plist %s/Info.plist ;
    '''%((pathSource,pathDen) * 12)

print order

chargePath = '~/Music/iTunes/iTunes\ Media/Mobile\ Applications/'

def replaceKo(string):
    name = ''
    for char in diffArr[0]:
        if char == ' ':
            name = name + '\ '
        else:
            name = name + char
    return name


def dealArr(arr):
    newArr = []
    mtimeDict = {}
    for ele in arr:
        ele = replaceKo(ele)
        mtimeDict[ele] = os.path.getmtime(chargePath + ele)

# 遍历文件夹
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
              mtime[file] = os.path.getmtime(file)  # 将每个文件的修改时间存为字典,拼接到数组最后面
    filelist.append(mtime)
    return filelist


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

# 打开itune并监控是否有新文件产生
def chargeItune():
    nextOrder = int(raw_input('打开iTune? YES:1 , NO:0 : '))
    if nextOrder == 1:
        openItuneFinder = ' open /Applications/iTunes.app '
        os.system(openItuneFinder)
        chargeTheFile = ' cd %s; ls' % chargePath
        originArr = os.popen(chargeTheFile).readlines()
        flag = True
        excuteTime = 0
        stepTime = 3
        while flag:
            excuteTime += stepTime
            if excuteTime > 300:
                flag = False
                print 'out of time and exit'
            time.sleep(stepTime)
            newArr = os.popen(chargeTheFile).readlines()
            if len(originArr) < len(newArr):
                diffArr = list(set(newArr).difference(set(originArr)))
                name = ''
                for char in diffArr[0]:
                    if char == ' ':
                        name = name + '\ '
                    else:
                        name = name + char
                print chargePath + name
                newFilePath = chargePath + name
                newFileSavePath = '/Users/Longcq/Documents/excellence_file/Tank资料/谭其伟_交接内容/近期出包备份/'
                cpNewFile = 'cp %s %s' % (newFilePath[:-1], newFileSavePath)
                print cpNewFile
                if os.system(cpNewFile) == 0:
                    flag = False
                    os.popen('open %s' % newFileSavePath)
                    print 'find the new file and success backup the new file'
                else:
                    print 'find the new file but failed backup'
                    # elif len(originArr) == len(newArr):
                    # for file in newArr:
                    #     if os.path.getmtime(chargePath + )

if os.system(order) == 0:
    print '----->>>success<<<-----\n'
else:
    print '----->>>failed<<<------\n'

