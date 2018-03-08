#!/usr/bin/python
#-*-coding:UTF-8-*-

import urllib2,re,os,urllib
import urlparse
import time
import threading
import Queue
import sys

redStr = '\033[31m'
greenStr = '\033[32m'
yellowStr = '\033[33m'
clearColorStr = '\033[0m'


save_root_path='/Users/admin/Desktop/test/chouti/111/'
all_task_count=0
complete_task_count=0
downloadConsule_flag=True



#重写thread的方法,以便增加回调
class WorkerThread(threading.Thread):
    def __init__(self, callback, target, name, args, startTime):
        super(WorkerThread, self).__init__()
        self.target= target
        self.callback = callback
        self.name = name
        self.args = args
        self.startTime = startTime
    
    #重写run方法,在target方法之后添加回调
    def run(self):
        self.target(self.args[0],self.args[1],self.args[2])
        self.callback(self.args[1],self.args[2],self.startTime)

#线程结束之后的回调信息
def callback(str,content,startTime):
    global complete_task_count
    complete_task_count=complete_task_count+1
    print greenStr + '下载完成: %s --大小: %.2fM -- 耗时:%.2fs \n'%(str, content,(time.time()-startTime))+ clearColorStr

#总体下载情况打印控制输出
def downloadConsule():
    flag=True
    while flag:
        global all_task_count,complete_task_count
        if not all_task_count == complete_task_count:
            print greenStr+'目前共有%s个任务,已完成%s个任务'%(all_task_count,complete_task_count)+clearColorStr
            time.sleep(10)
        else:
            if all_task_count>0:
                print greenStr+'目前共有%s个任务,已完成%s个任务'%(all_task_count,complete_task_count)+clearColorStr
                flag=False


#通过url获得网页源代码
def getUrlRespHtml(url):
    # 要设置请求头，让服务器知道不是机器人
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    request = urllib2.Request(url, headers=headers)
    #尝试去获取网页源代码
    try:
        html = urllib2.urlopen(request)
        return html.read()

    except Exception, e:
        print redStr+'获取:%s 的源代码出错,错误原因:%s'%(url,e)+clearColorStr
        return None

#单页N个作品处理
def funHome(html,index,dir_page):
    actor = re.findall('<img src=\"http[s]?://.*?\"',html)

    actor = list(set(actor))
#    print len(actor)
    nameIndex=0
#    print "-----star write-----"
    file_root_path = save_root_path + dir_page
    if not os.path.exists(file_root_path):
        os.mkdir(file_root_path)
    for ele in actor:
        with open(file_root_path + '/save.txt', "a") as code:
            # 剔除"未命名_副本.png"的多余链接
            if '未命名_副本.png' in ele or 'img.t.sinajs.cn/t35' in ele or '.html' in ele or 'ww1.sinaimg.cn/large/' in ele:
                continue
            code.write(ele[10:-1])
            code.write('\n')

##########------暂不用(开始)-------##############
#!!目前无法解决多个文件下载进度问题
#下载进度刷新
def report(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write(yellowStr + "\r ....已下载: %d%%  \r" % percent + clearColorStr)
    sys.stdout.flush()

##########------暂不用(结束)-------##############

#通过url下载图片
def downloadImageWithUrl(f,save_path,content):
    with open(save_path, 'wb') as code:
        code.write(f.read())
# 下载进度显示,暂不用
#    sys.stdout.write(yellowStr + '\r正在下载: ' + save_path + '...\n' + clearColorStr)
#    urllib.urlretrieve(url, save_path, reporthook=report)
#    sys.stdout.write(greenStr + "\r下载完成, 保存到 %s,文件大小:%sM" % (save_path,content) + '\n\n' + clearColorStr)
#    sys.stdout.flush()


#单个.html,然后获取所有页数的图片并下载
def startWithUrl(sourceUrl):
    print '正在处理的.html为: %s'%sourceUrl
    # 当线程数太多(超过10个,这里与最大下载数不一样)时等待5秒再处理单个作品的.html页面
    while threading.activeCount() > 10:
        time.sleep(5)
    #初始化下载打印
    global downloadConsule_flag
    downloadConsule_flag=True
    #1.提取网页中的jpg的url,并且写入txt文件中
    #sourceUrl="https://9deers.com/ipz-193.html/"
    #提取番号名称,并以此作为文件夹名称
    dir_page = re.search('\w*-\w*.html',sourceUrl).group()[:-5]

    if not os.path.exists('%s%s/save.txt'%(save_root_path,dir_page)):
        firstPageHtml = getUrlRespHtml(sourceUrl)
        #print firstPageHtml
        for ele in range(1,100):
            url = sourceUrl + '%s'%ele
            currentPageHtml = getUrlRespHtml(url)
            if firstPageHtml == currentPageHtml and ele > 1:
                break
#            print '正在写入****%s***到txt中'%url
            funHome(currentPageHtml,ele,dir_page)
#  页数判断开始----
#    if not os.path.exists('%s%s/save.txt'%(save_root_path, dir_page)):
#        #获取单个.html所有页数的图片的url,因此得在后面加上页数,但是页数未知,当下一页和上一页相同时,表示已经完成遍历
#        lastPageHtml = getUrlRespHtml(sourceUrl+'70')
##        print 'lastPageHtml: %s'%(len(lastPageHtml))
#        for ele in range(1,100):
#            url = sourceUrl + '%s'%ele
#            currentPageHtml = getUrlRespHtml(url)
##            print 'prePageHtml: %s'%(len(prePageHtml))
##            print 'currentPageHtml: %s'%(len(currentPageHtml))
#            if len(currentPageHtml) == len(lastPageHtml) and ele > 1:
#                break
##            print '正在写入****%s***到txt中'%url
#            funHome(currentPageHtml,ele,dir_page)
    #2,查重txt,去掉重复的url
    txtStr=''
    repeatFlat=True
    with open('%s%s/save.txt'%(save_root_path, dir_page), "r") as code:
        txtStr=code.readlines()
        if not len(txtStr) == len(list(set(txtStr))):
            repeatFlat=False
            txtStr=list(set(txtStr))
    if repeatFlat == False:
        with open('%s%s/save.txt'%(save_root_path, dir_page), "w") as code:
            for readline in txtStr:
                print '正在写入****%s***到txt中'%readline
                code.write(readline)
#页数判断结束----
    #3,根据txt里面的每一条url去新建线程下载图片
    with open('%s%s/save.txt'%(save_root_path, dir_page), "r") as code:
        index = 0
        for readline in code.readlines():
             #排除一些不合适的.html
             if 'video' in readline or 'haha' in readline or'daidai' in readline:
                continue
             index = index + 1
             # 当线程数太多时等待5秒再新开线程,这里限定最多50个下载并发
             while threading.activeCount() > 50:
                time.sleep(5)
             #下载文件路径
             save_path = '%s%s/%s_%s.jpg'%(save_root_path,dir_page,dir_page,index)
             #尝试去获取url内容,可能会出错
             try:
                f=urllib2.urlopen(readline,timeout=20)
             except Exception, e:
                print redStr+'当前图片:%s --打开出错,错误原因: %s'%(readline,e)+clearColorStr
                continue
             #通过请求头获得图片大小
             try:
                content=float(dict(f.headers)['content-length']) /1024/1024
                #过滤掉小于10k的照片
                if content < 0.17:
                    print '当前图片:%s--小于170k,忽略'%(save_path)
                    continue
             except Exception, e:
                print redStr+'当前图片:%s --无法获得content-length,错误原因: %s'%(readline,e)+clearColorStr
                content=0
             #如果文件已存在,再判断是否下载完整,没有下载完整则重新下载,否则无需再次下载
             if os.path.exists(save_path):
                down_size=os.path.getsize(save_path)
                if not content == down_size:
                    print '目标文件已存在并下载完整: %s -- 图片大小: %.2fM'%(save_path,content)
                    continue
             print yellowStr + '正在下载图片......%s -- 图片大小: %.2fM'%(save_path,content) + clearColorStr
             
             global all_task_count
             all_task_count=all_task_count+1
             if downloadConsule_flag:
                 downloadConsule_flag=False
                 thread=threading.Thread(target=downloadConsule)
                 thread.start()

             # 每个页面创建一个线程去下载
             start_time=time.time()
             thread = WorkerThread(target=downloadImageWithUrl,args=(f,save_path,content),name="child_thread_%s"%(index),callback=callback,startTime=start_time)
             thread.start()


#通过搜索获取众多html网页,然后分析单个html并下载
def getSearchHomePageHtml(keyworld):
#    file_root_path = '/Users/admin/Desktop/test/chouti'
    keyworld_txt_path=save_root_path + 'homeUrl_%s.txt'%keyworld
#    firstPageHtml=''
    if not os.path.exists(keyworld_txt_path):
        for number in range(1,100):
            print'正在处理搜索"%s"的第%s页'%(keyworld,number)
            homeUrl='https://9deers.com/page/%s?s=%s'%(number,keyworld)
            #尝试去获取网页源代码
            currentPageHtml = getUrlRespHtml(homeUrl)
            if currentPageHtml == None:
                return
#            if number == 1:
#                firstPageHtml=currentPageHtml
#            
#            if firstPageHtml == currentPageHtml and number > 1:
#                continue
            actor = re.findall('https://9deers.com/\w*-\w*.html',currentPageHtml)
                
            actor = list(set(actor))
            print len(actor)
            nameIndex=0
            if not os.path.exists(save_root_path):
                os.mkdir(save_root_path)
            for ele in actor:
                print ele
                with open(keyworld_txt_path, "a") as code:
                    code.write(ele+'/'+'\n')


    #2,根据txt里面的每一条html去触发startWithUrl()方法
    with open(keyworld_txt_path, "r") as code:
        index = 0
        for readline in code.readlines():
            startWithUrl(readline.strip('\n'))


#getSearchHomePageHtml('rio')
getSearchHomePageHtml('樱空桃')
#startWithUrl('https://9deers.com/gif-355.html/')
#startWithUrl('https://9deers.com/ipz-193.html/')
#keyword_input=raw_input('请输入关键字: ')
#if keyword_input:
#    getSearchHomePageHtml(keyword_input)

#downloadConsule()

