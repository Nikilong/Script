#!/usr/bin/env python
#coding:utf-8

import os,shutil
path = '/Users/admin/Desktop/kw_前田'
#shutil.move('/Users/admin/Desktop/kw_桃谷/idbd-574/idbd-5741.jpg','/Users/admin/Desktop/kw_桃谷/collect/idbd-5741.jpg')
#一级目录展开
for file in os.listdir(path):
    
    if '.DS_Store' in file or '.txt' in file:
        continue
    #二级目录展开
    for ele in os.listdir(os.path.join(path,file)):
        if '.DS_Store' in ele or '.txt' in ele:
            continue
#        print os.path.join((path+'/'+file),ele)
#        print os.path.join((path+'/'+file),(file+ele))
        #为1.jpg加上文件夹名称作为前缀
        os.rename(os.path.join((path+'/'+file),ele),os.path.join((path+'/'+file),(file+'_'+ele)))


