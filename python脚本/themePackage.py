#!/usr/bin/env python
#coding:utf-8

import os,sys,zipfile,shutil

#使用方法:1.cd到根目录(iExOA4iPhoneSkin.xml);2,指定zip_name和输出保存的save_path
#zip_name='iphone蓝色主题-2.zip'
#save_path='/Users/Longcq/Desktop/test'
zip_name=sys.argv[1]
save_path=sys.argv[2]

#删除旧的压缩文件
old_zip_path='%s/%s'%(save_path,zip_name)
if os.path.exists(old_zip_path):
    os.remove(old_zip_path)

#压缩文件
f = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)
startdir = './'
for dirpath, dirnames, filenames in os.walk(startdir):
    for filename in filenames:
        if '.DS_Store' in filename or zip_name in filename:
            continue
#        print os.path.join(dirpath,filename)
        f.write(os.path.join(dirpath,filename))
f.close()

#将新的压缩文件移动出来
new_zip_path='./%s'%zip_name
if os.path.exists(new_zip_path):
    shutil.move(new_zip_path,save_path)



