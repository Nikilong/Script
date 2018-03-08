#!/usr/bin/env python
#coding:utf-8

import urllib2,urllib,os

# 通过url下载网页的源代码
def getHtmlFromUrl(url):
    # 要设置请求头，让服务器知道不是机器人
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url,headers=headers)
    html = urllib2.urlopen(request).read()
    print html

    save_path = '/Users/Longcq/Desktop/test/666/'
    file_name = '3.html'
    if not os.path.exists(save_path):
        #makedirs可以创建多级目录,即test不存在时创建test文件并在test文件夹内创建66文件夹,而mkdir只会创建一个文件夹,当test文件夹不存在时会报错
        os.makedirs(save_path)
    save_path = save_path + file_name
    with open(save_path,'w') as f:
        f.write(html)

# 通过url下载图片
def getImgFromUrl(url):
    #urlopen之后是一个object对象,得通过read()读取出来
    img = urllib.urlopen(url)
    # 图片和视频需要转为二进制的文件,采用wb模式,write-binary
    with open('/Users/Longcq/Desktop/test/3.jpg','wb') as f:
        f.write(img.read())

# getHtmlFromUrl('http://www.baidu.com')
# getImgFromUrl('http://172.20.105.89:8090/SSH/images/resign_background.jpg')

#创建多级文件夹
# for ele in range(1,10):
#     save_path = '/Users/Longcq/Desktop/test/666/' + '%s'%ele
#     if not os.path.exists(save_path):
#         os.makedirs(save_path)
#     save_path = save_path + '/test.txt'
#     with open(save_path,'w') as f:
#         f.write('hello world')


#正则表达式
import re
#match是从字符串的开头开始寻找,像下面的字符串例子必须匹配s开头的
m = re.match('od', 'seafood')
if m is not None: print("match-" + m.group())

#search是在字符串整体中开始寻找
m = re.search('od', 'seafood')
if m is not None: print("search-" + m.group())

