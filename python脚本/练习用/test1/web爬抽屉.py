#!/usr/bin/python
#-*-coding:UTF-8-*-

import urllib2,re,os,urllib
#import requests
import urlparse
import time
import threading
import Queue


def getUrlRespHtml(url):
    heads = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Charset': 'GB2312,utf-8;q=0.7,*;q=0.7',
             'Accept-Language': 'zh-cn,zh;q=0.5',
             'Cache-Control': 'max-age=0',
             'Connection': 'keep-alive',
             'Host': 'John',
             'Keep-Alive': '115',
             'Referer': url,
             'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.14) Gecko/20110221 Ubuntu/10.10 (maverick) Firefox/3.6.15'}

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    opener.addheaders = heads.items()
    respHtml = opener.open(req).read()
    return respHtml


#单页N个作品处理
def funHome(url,index):
    html = getUrlRespHtml(url)
    print '当前处理url:%s'%url
    
    #share-pic="http://img3.chouti.com/CHOUTI_20180118/EB6C5150205845F7A080300FCF634294_W200H200.jpg" share-title="白白" share-summary="" share-linkid="16783466"
    #share-pic="http://img3.chouti.com/CHOUTI_20180116/6918A763BB1842A1B55350A0397654A5_W395H229.jpg"
    actor = re.findall('share-pic=\"http://img3.chouti.com/.*?.jpg',html)
    actor = list(set(actor))
    print len(actor)
    nameIndex=0
    for ele in actor:
        nameIndex=nameIndex+1
#        print ele[11:]
        #提取文件名后缀并且拼接保存路径
        save_path = '%s%s_%s.jpg' %('/Users/admin/Desktop/test/chouti/',index,nameIndex)
        print save_path
        f = urllib.urlopen(ele[11:])
        with open(save_path, "wb") as code:
            code.write(f.read())


def fetch_img_func(q):
    while True:
        try:
            # 不阻塞的读取队列数据
            url = q.get_nowait()
            i = q.qsize()
        except Exception, e:
            print e
            break;
        print 'Current Thread Name Runing %s ... 11' % threading.currentThread().name
        funHome(url,url[-2:])


sourceUrl="http://dig.chouti.com/user/nainiu911/submitted/"
#funHome('http://dig.chouti.com/user/nainiu911/submitted/1',1)

## 使用Queue来线程通信，因为队列是线程安全的（就是默认这个队列已经有锁）
q = Queue.Queue()

#52ye
for index in range(35,52):
    name = '%s%s'%(sourceUrl,index)
    q.put(name)

    print name


start = time.time()
# 可以开多个线程测试不同效果
t1 = threading.Thread(target=fetch_img_func, args=(q,), name="child_thread_1")
t2 = threading.Thread(target=fetch_img_func, args=(q,), name="child_thread_2")
t3 = threading.Thread(target=fetch_img_func, args=(q,), name="child_thread_3")
t4 = threading.Thread(target=fetch_img_func, args=(q,), name="child_thread_4")
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

end = time.time()







