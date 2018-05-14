#!usr/bin/python
#coding:UTF-8

import sys,os
'''
    使用说明:可以传入两个参数,1.要统计的文件夹路径;2.特别指出的类前缀
'''

class CountModel:
#    pr_text_list = []  #每个文件信息数组
    file_count = 0      #文件个数统计
    totalLines = 0      #总行数统计
    def __init__(self,name):
        self.name = name        #模型名称
        self.pr_text_list = []  #每个文件信息数组
#        self.file_count = 0      #文件个数统计
#        self.totalLines = 0      #总行数统计

    def addFileMessage(self,text,lines):
        self.pr_text_list.append(text)
        self.file_count += 1
        self.totalLines += lines

    def talk(self):
        print '>>>>>组别:%s<<<<<\n   共有 %s 个文件  共计 %s 行'%(self.name,self.file_count,self.totalLines)

# 前缀过滤
if len(sys.argv) > 2:
    preName = sys.argv[2]
else:
    preName = 'XM'


# 根据行数分组打印
model_hundred = CountModel('0--100行')
model_fiveHundred = CountModel('100--500行')
model_thousand = CountModel('500--1000行')
model_fiveThousand = CountModel('1000--5000行')
model_tenThousand = CountModel('5000--10000行')
model_large = CountModel('10000行以上')
model_xm = CountModel('%s文档'%preName)
model_list = [model_hundred,model_fiveHundred,model_thousand,model_fiveThousand,model_tenThousand,model_large]

for rootPath,dir,files in os.walk(sys.argv[1]):
    for file in files:
        # 过滤关键字
        filterList = ['DS_Store','.xc','.svn']
        in_list = [_ for _ in filterList if _ in file]
        if len(in_list) > 0:
            continue
        #过滤格式
        filterEXList = ['.a','.png','.jpg','.jpeg','.json','.pack','.idx','.pbxproj']
        in_exlist = [_ for _ in filterEXList if file.endswith(_)]
        if len(in_exlist):
            continue
        # 不带后缀的排除掉
        if not '.' in file:
            continue
        f = open(os.path.join(rootPath,file))
        lines = len(f.readlines())
        # 另外统计XM前缀类的文件
        if file.startswith(preName):
            print file
            print '++++'
            model_xm.addFileMessage('文件:%s ---- 行数:%s'%(file,lines),lines)
        #根据行数添加进对应的数组
        if lines < 100:
            model_hundred.addFileMessage('文件:%s ---- 行数:%s'%(file,lines),lines)
        elif lines < 500:
            model_fiveHundred.addFileMessage('文件:%s ---- 行数:%s'%(file,lines),lines)
        elif lines < 1000:
            model_thousand.addFileMessage('文件:%s ---- 行数:%s'%(file,lines),lines)
        elif lines < 5000:
            model_fiveThousand.addFileMessage('文件:%s ---- 行数:%s'%(file,lines),lines)
        elif lines < 10000:
            model_tenThousand.addFileMessage('文件:%s ---- 行数:%s'%(file,lines),lines)
        else:
            model_large.addFileMessage('文件:%s ---- 行数:%s'%(file,lines),lines)
        f.close()
# 统计总行数
totalLines = 0
totalFile_count = 0
for model in model_list:
    print '\n\n'
    model.talk()
    totalLines += model.totalLines
    totalFile_count += model.file_count
    for ele in model.pr_text_list:
        print ele
print '\n\n================分割线================'
for model in model_list:
    model.talk()
model_xm.talk()
print '================分割线================'
print '统计结果,共 %s 行,共 %s 个文件\n其中%s文件行数共 %s行 共:%s 个文件 \n文件路径:%s'%(totalLines,totalFile_count,preName, model_xm.totalLines,model_xm.file_count, sys.argv[1])

