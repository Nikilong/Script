#!/usr/bin/python
#-*-coding:UTF-8-*-

import urllib2,re,os,urllib
import urlparse
import time
import threading
import Queue

class WorkerThread(threading.Thread):
    def __init__(self, callback, target):
        super(WorkerThread, self).__init__()
        self.target= target
        self.callback = callback

    def run:
        self.target()
        self.callback()

#通过url获得网页源代码
def getUrlRespHtml(url):
    # 要设置请求头，让服务器知道不是机器人
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    request = urllib2.Request(url, headers=headers)
    html = urllib2.urlopen(request).read()
    return html


#单页N个作品处理
def funHome(url,index,dir_page):
    html = getUrlRespHtml(url)
    actor = re.findall('<img src=\"http[s]?://.*?\"',html)

    actor = list(set(actor))
#    print len(actor)
    nameIndex=0
#    print "-----star write-----"
    file_root_path = '/Users/admin/Desktop/test/chouti/' + dir_page
    if not os.path.exists(file_root_path):
        os.mkdir(file_root_path)
    for ele in actor:
        with open(file_root_path + '/save.txt', "a") as code:
            # 剔除"未命名_副本.png"的多余链接
            if '未命名_副本.png' in ele or 'img.t.sinajs.cn/t35' in ele or '.html' in ele or 'ww1.sinaimg.cn/large/' in ele:
                continue
            code.write(ele[10:-1])
            code.write('\n')



#通过url下载图片
def downloadImageWithUrl(url,nameIndex,dir_page):
    save_path = '/Users/admin/Desktop/test/chouti/%s/%s.jpg'%(dir_page,nameIndex)
    print '正在下载图片:%s'%save_path
    f = urllib.urlopen(url)
    with open(save_path,'wb') as code:
        code.write(f.read())


#单个.html,然后获取所有页数的图片并下载
def startWithUrl(sourceUrl):
    print sourceUrl
    # 当线程数太多(超过10个,这里与最大下载数不一样)时等待5秒再处理单个作品的.html页面
    while threading.activeCount() > 10:
        time.sleep(5)
#    return
    #1.提取网页中的jpg的url,并且写入txt文件中
    #sourceUrl="https://9deers.com/ipz-193.html/"
    dir_page = re.search('\w*-\w*.html',sourceUrl).group()[:-5]

    if not os.path.exists('/Users/admin/Desktop/test/chouti/%s/save.txt'%dir_page):
        firstPageHtml = getUrlRespHtml(sourceUrl)
        #print firstPageHtml
        for ele in range(1,100):
            url = sourceUrl + '%s'%ele
            currentPageHtml = getUrlRespHtml(url)
            if firstPageHtml == currentPageHtml and ele > 1:
                break
            print '正在写入****%s***到txt中'%url
            funHome(url,ele,dir_page)


    #2,根据txt里面的每一条url去新建线程下载图片
    with open('/Users/admin/Desktop/test/chouti/%s/save.txt'%(dir_page), "r") as code:
        index = 0
        for readline in code.readlines():
             print '---'
             #        print readline
             index = index + 1
             # 当线程数太多时等待5秒再新开线程,这里限定最多50个下载并发
             while threading.activeCount() > 50:
                time.sleep(5)

             # 每个页面创建一个线程去下载
             thread = threading.Thread(target=downloadImageWithUrl,args=(readline,index,dir_page),name="child_thread_%s"%(index))
             thread.start()


#通过搜索获取众多html网页,然后分析单个html并下载
def getSearchHomePageHtml(keyworld):
    file_root_path = '/Users/admin/Desktop/test/chouti'
    keyworld_txt_path=file_root_path + '/homeUrl_%s.txt'%keyworld
    if not os.path.exists(keyworld_txt_path):
        for number in range(1,100):
            print'正在处理搜索"%s"的第%s页'%(keyworld,number)
            homeUrl='https://9deers.com/page/%s?s=%s'%(number,keyworld)
            try:
                currentPageHtml = getUrlRespHtml(homeUrl)
            except Exception, e:
                print e
                return

            actor = re.findall('https://9deers.com/\w*-\w*.html',currentPageHtml)
                
            actor = list(set(actor))
            print len(actor)
            nameIndex=0
            if not os.path.exists(file_root_path):
                os.mkdir(file_root_path)
            for ele in actor:
                print ele
                with open(keyworld_txt_path, "a") as code:
                    code.write(ele+'/'+'\n')


    #2,根据txt里面的每一条html去触发startWithUrl()方法
    with open(keyworld_txt_path, "r") as code:
        index = 0
        for readline in code.readlines():
            print readline
#            print '正在处理"%s"的信息'%readline
            startWithUrl(readline.strip('\n'))


#getSearchHomePageHtml('rio')
#getSearchHomePageHtml('lai')
startWithUrl('https://9deers.com/gif-358.html/')

#keyword_input=raw_input('请输入关键字: ')
#if keyword_input:
#    getSearchHomePageHtml(keyword_input)

