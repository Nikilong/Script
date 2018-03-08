#!/usr/bin/env python
#-*-coding:UTF-8-*-
#FileName:test_1.py

# i=5
# print i
# i=i+1
# print i
# print i == 5
# s='''this
# \'s
# long
# string
# '''
# print s

# long = 4
# heig = 5
# long = 6
# area = long * heig
# print "area is \n",area

# num = 20
# put = int(raw_input('please input a integer '))
# if num > put:
#     print 'lower'
# elif num == put:
#     print 'bingo'
# else:
#     print 'bigger'

# num2 = 33
# flat = True
# while flat:
#     put = int(raw_input("guess a integer "))
#     print put
#     if put == num2:
#         print 'bingo'
#         flat = False
#     elif put > num2:
#         print 'too big'
#     else:
#         print 'too small'
# # else:
# #     print 'the loop is end'
#
# print 'done'

# is equal to for for (int i = 0; i < 5; i++)
# for i in range(1,60,1):
#     print i
# else:
#     print 'end loop'

# while True:
#     s = raw_input('input something ')
#     if s == 'quit':
#         break
#     print 'length of input string is ',len(s)
# else:
#     print 'end loop'
# print 'done'


# while True:
#     s = raw_input('input something: ')
#     if s == 'quit':
#      break
#     if len(s) < 3:
#      continue
#     print 'go on'
# print 'done'


# def sayHello():
#  print 'hello word'
#
# print 'will star'
# sayHello()

# def maxNum(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print 'will star'
# a = int(raw_input('input a interge: '))
# b = int(raw_input('input anthor interger:'))
# c = maxNum(a,b)
# print 'the bigger one is ',c

# def funC(x):
#     print 'x is ',x
#     x = 2
#     print 'x change to ',x
#
# x = 59
# funC(x)
# print 'the last x is ',x


# def func():
#     global x
#     print 'x is ',x
#     x = 2
#     print 'x change to ',x
#
# x = 50
# func()
# print 'x finally is ',x



# def say(str, time = 1):
#     print str * time
# say('hello')
# say('world',6)



# def max(a,b):
#     '''
#     It will select the max number between two interger.
#        You must
#     '''
#     if a > b:
#         print 'the biger is ',a
#     else:
#         print 'the biger is ',b
#
# max(88,66)
# print max.__doc__


# import sys
# print 'The command line arguments are:'
# for i in sys.argv:
#  print i
# print '\n\nThe PYTHONPATH is', sys.path, '\n'

# if __name__ == '__main__':
#     print 'excute itself'
# else:
#     print 'being imported'


# a = ['appl', 'banane', 'ca' , 'mo', 'dd']
# print 'begin',a
# for itm in a:
#     print itm
# for itm in a:
#     print itm,
# a.append('ee')
# print 'append',a
# a.sort()
# print 'sort',a
# del a[3]
# print 'delete',a

# zoo = ('aa','bb','cc')
# print 'old zoo has',zoo
# new_zoo = ('n_aa','n_bb',zoo)
# print 'new zoo has',new_zoo
# print 'old zoo second ani is',zoo[2]
# print 'new zoo forth ani is ',new_zoo[2][2]

# print '%s is %d year old' %('Jack',55)

# name = 'swarpoop'
# if 'r' in name:
#     print 'the string has r'
#
# if name.find('op') != -1:
#     print 'the string has op'
#
# dett = '_**_'
# arr = ['aaa','bbb','ccc']
# print dett.join(arr)


# import os
# name = 'cd /Users/admin/Desktop/Classes'
# if os.system(name) == 0:
#     print 'success to cd'
# namee = name + ';' + 'touch pyhon222.text'
# # print namee
# if os.system(namee) == 0:
#     print 'touch success'

#输入一个文件夹的路径,然后再该路径之下创建一个text文件
# import os
# import time
# path = str(raw_input('file path: '))
# print path
# name = 'cd %s ;touch %s.text' %(path,time.strftime('%Y%m%d%H%M%S'))
# if os.system(name) == 0:
#     print 'success'
# else:
#     print 'failed'
# namee = 'cd ' + path +'open ./'
# os.system(namee)


import os
import time

# path = raw_input('输入需要检测的文件夹路径: ')
# name = 'cd %s; ls '%path
# print name

# def detector(dir, sec):
#     origin = set([_f[2] for _f in os.walk(dir)][0])
#     time.sleep(sec)
#     final = set([_f[2] for _f in os.walk(dir)][0])
#     return final.difference(origin)
# while (!detetor(path))


# var = os.popen('ls').read()
# print var


# print eval('3 * 4')
# a=1
# g={'a':20,'b':10}
# print eval("a+b",g)
# # exec 'print "hello word"'




# import urllib
# import urllib2
# url = "http://www.baidu.com"
#
# req = urllib2.Request(url)
# print req
#
# res_data = urllib2.urlopen(req)
# res = res_data.read()
# print res


#调用默认浏览器打开网址
# import sys
# import webbrowser
#
# url = 'http://www.baidu.com'
# webbrowser.open(url)
# print webbrowser.get()



import urllib
import urllib2
import re

#根据url获取网页信息
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getURLARR(url):
    try:
        page = urllib.urlopen(url)
        htmlG = page.read()
        return re.findall('https*://[^\"^)]*[^(\.js)]\"',htmlG)  #以http或者https开头,以"结尾,删除.js类型,中间不包含"
    except:
        print 'error'

# html = getHtml("http://www.baidu.com/")
# http://news.baidu.com

# print html
# html = 'src="http://www baidu ncom .com"'
# searchArr = re.findall('src=\"http://([a-z]*|[0-9]*|/*|.*)\"',html)
# print '\n'.join(searchArr)
# searchArr = re.findall('http://([a-z]*[A-Z]*[0-9]*)\.png',html)
# http://static.tieba.baidu.com/tb/editor/images/client/image_emoticon4.png\" >","user_id":98
# searchArr = re.findall('https*://[^\"^)]*[^(\.js)]\"',html)  #以http或者https开头,以"结尾,删除.js类型,中间不包含"
# index = 0



