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

#当个作品具体处理
def getHtmlImgs(url,index):
    html = getUrlRespHtml(url)
    print '当前第%s页的个人作品url:%s'%(index,url)
    # 文件夹名称,从<h1></h1>中findall,取第一个元素(唯一元素),该元素是字符串,因此可以切片把首尾的<h1></h1>去掉
    file_root_path = re.findall('<h1>.*?</h1>',html)[0][4:-6]
    file_root_path = '/Users/admin/Desktop/test/img/'+ '%s'%index  + file_root_path
#    print file_root_path
#    return
    if not os.path.exists(file_root_path):
        os.mkdir(file_root_path)
#    print html
    # 将图片的网址提取出来\d表示1-9数字,\D表示匹配非数字,\w代表数字和大小写字母和下划线[a-z0-9A-Z_],\W等同于[^a-z0-9A-Z_]等同\w取非,+表示至少出现一次,*表示出现一次或者零次
#src="https://www.mgsbuy.net/wp-content/uploads/2018/02/cap_e_0_259luxu-921.jpg"
#src="https://www.mgsbuy.net/wp-content/uploads/2018/01/ddute-664-6.jpg
    imgUrlArr = re.findall('https://www.mgsbuy.net/wp-content/uploads/\d+/\d+/\w+[-\d]*.jpg',html)
#    imgUrlArr = re.findall('https://www.mgsbuy.net/wp-content/uploads/\d+/\d+/.+?.jpg',html)
    imgUrlArr = list(set(imgUrlArr))

    # 遍历数组
    for ele in imgUrlArr:
#        print ele
        #提取文件名后缀并且拼接保存路径
        img_name = re.findall('/\w[-\w]*.jpg',ele)[0]
        save_path = '%s%s' %(file_root_path,img_name)
        print save_path
        f = urllib.urlopen(ele)
        with open(save_path, "wb") as code:
            code.write(f.read())

#undo
#        res = requests.get(ele, stream=True)
#    
#        if res.status_code == 200:
#        #提取文件名后缀并且拼接保存路径
#            img_name = re.findall('/\w[-\w]*.jpg',ele)[0]
#            save_path = '%s%s' %(file_root_path,img_name)
#                # 保存下载的图片
#            with open(save_path, 'wb') as fs:
#                for chunk in res.iter_content(1024):
#                    fs.write(chunk)
#                print 'save %s pic ' % i

#单页N个作品处理
def funHome(url,index):
    html = getUrlRespHtml(url)
    print '当前处理url:%s'%url
    
    #https://www.mgsbuy.net/200gana-1591.html
    actor = re.findall('https://www.mgsbuy.net/.*.html',html)
    actor = list(set(actor))
    
    for ele in actor:
        getHtmlImgs(ele,index)
    #将url写入到txt文件中
#    f = open('/Users/admin/Desktop/dong.txt','a')
#    str='\n'.join(actor)
#    f.write(str)
#    f.close()


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



#getHtmlImgs('https://www.mgsbuy.net/259luxu-921.html')
sourceUrl="https://www.mgsbuy.net/page/"
#funHome('https://www.mgsbuy.net')

# 使用Queue来线程通信，因为队列是线程安全的（就是默认这个队列已经有锁）
q = Queue.Queue()

for index in range(12,20):
    name = '%s%s'%(sourceUrl,index)
    q.put(name)

    print name


start = time.time()
# 可以开多个线程测试不同效果
t1 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_1")
t2 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_2")
t3 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_3")
t4 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_4")
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

end = time.time()







