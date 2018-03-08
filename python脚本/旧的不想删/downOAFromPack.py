#!/usr/bin/python
#coding:UTF-8

import os,re,sys,urllib2,urllib,ssl,time

from os.path import basename
from urlparse import urlsplit

# 获取网页源代码
def getUrlRespHtml(url):
    #全局取消证书验证
    ssl._create_default_https_context = ssl._create_unverified_context
    # 要设置请求头，让服务器知道不是机器人
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    headers = {'User-Agent': user_agent}
    
    request = urllib2.Request(url, headers=headers)
    #尝试去获取网页源代码
    try:
        html = urllib2.urlopen(request)
        return html.read()
    
    except Exception, e:
        print '[error]:%s'%e
        return None

# 通过url获取文件正式名称
def realNameFromUrl(url, passName=None):
    if passName:
        fileName = passName
        urllib.urlretrieve(attachURL, fileName)
    else:
        #http://stackoverflow.com/questions/862173/how-to-download-a-file-using-python-in-a-smarter-way
        r = urllib.urlopen(url)
        if r.info().has_key('Content-Disposition'):
            fileName = r.info()['Content-Disposition'].split('filename=')[1]
            fileName = fileName.replace('"', '').replace("'", "")
        elif r.url != url:
            # if we were redirected, the real file name we take from the final URL
            fileName = basename(urlsplit(r.url)[2])
    return fileName

# 解析项目配置文件夹的xml文件
def dealXml(path):
    result_list = []
    with open(path,'r') as f:
        for line in f.readlines():
            if 'serverAddress' in line:
                result_list.append(line)

    print '\n--->初步提取到的serverAddress有%s个'%len(result_list)
    if len(result_list) == 1:
        print '初步提取到的serverAddress是 %s'%result_list[0]
        return result_list[0]
    elif len(result_list) == 2:
        # 有些项目分为内外网,例如'eq_二汽_不要端口'就分内网和外网
        # 但是可能存在有注释掉的多余的serverAddress的bug
        for ele in result_list:
            print '初步提取到的serverAddress是 %s'%ele
            if ' displayName=\"外网\"' in ele:
                return ele
    elif len(result_list) > 2:
        print '!!!!!初步提取到的serverAddress过多,无法确认'
        for ele in result_list:
            print '初步提取到的serverAddress是 %s'%result_list[0]
        print '目录: %s\n*******结束*******'%path
        exit(0)
    return None

#1.提取打包配置文件中的url
path = '%s/iOS/'%sys.argv[1]
# 提取项目文件名
projectName = re.findall('ProjectPackage/.*',sys.argv[1])[0][15:]
maspApp_url = ''

if os.path.exists(path):
    #在终端打印initConfig.xml文件
    path = path + '/initConfig.xml'
    os.system('cat \'%s\''%path)
    serverAddress_str = dealXml(path)
#    # 有些项目分为内外网,例如'eq_二汽_不要端口'
#    print '\n提取到%s个初始化地址'%len(serverAddress_list)
    if not serverAddress_str == None:
#        for serverAddress_str in serverAddress_list:
        url_list=re.findall('\"http.*?\"',serverAddress_str)
        
        if len(url_list)>0:
            url=url_list[0][1:-1]
            print '\n--->最终提取到初始化地址为:'+url
            maspApp_url = '%s/masp/app'%(url)
        else:
            print '\n!!!!该项目iOS打包配置初始化地址为空 \n*******结束*******'
            exit(0)
    else:
        print '\n!!!!该项目iOS打包配置初始化地址为空 \n*******结束*******'
        exit(0)

else:
    print '!!!!该项目没有iOS的打包配置 \n*******结束*******'
    exit(0)
#2.通过支撑平台下载页面来下载客户端
#html = getUrlRespHtml('https://iexoa.nbport.com.cn/masp/app/applist.jsp')
print '--->尝试连接 %s ....'%maspApp_url

html = getUrlRespHtml(maspApp_url)
iOS_list = []
iOS_fileName_list = []
if not html == None:
    result_list = re.findall('itms-services://.*?\"',html)
    if len(result_list) > 0:
        for ele in result_list:
            # 获得xml的url
            result_xml = re.findall('http.*',ele)[0][:-1]
            # 从xml获得iOS客户端下载链接、版本号、以及名称
            xml_html = getUrlRespHtml(result_xml)
            # xml中的url可能是[]也可能没有[]
            iOS_url_result_list = re.findall('http.*?]',xml_html)
            if len(iOS_url_result_list) == 0:
                iOS_url_result_list = re.findall('http.*?<',xml_html)
            iOS_url = iOS_url_result_list[0][:-1]
            iOS_name = re.findall('<string>.*?</string>',xml_html)[-1]
            if '![CDATA[' in iOS_name:
                iOS_name = iOS_name[17:-12]
            else:
                iOS_name = iOS_name[8:-9]
            iOS_list.append(iOS_url)
            iOS_fileName_list.append(iOS_name)
            print '从XML文件: %s \n提取到文件: %s   \n下载URL:%s\n'%(result_xml,iOS_name, iOS_url)
else:
    print '无法从%s获得内容 \n*******结束*******'%maspApp_url
    exit(0)

# 获得时间戳 03-06_10:07拼接文件路径,pack是证明从项目打包配置文件下载的客户端
timeStr = time.strftime('%m-%d_%H:%M',time.localtime())
dir_path = '/Users/Longcq/Downloads/jenkins下载/pack_%s_%s'%(projectName,timeStr)

if not os.path.exists(dir_path):
    os.mkdir(dir_path)


# 下载客户端
downCount = len(iOS_list)
if downCount > 0:
    print '--->共有%s个客户端需要下载,正在下载中........'%downCount
    for ele in range(0,downCount):
        url = iOS_list[ele]
        save_dir_path = '%s/%s'%(dir_path,iOS_fileName_list[ele])
        if not os.path.exists(save_dir_path):
            os.makedirs(save_dir_path)
        file = urllib.urlopen(url)
        with open(os.path.join(save_dir_path,realNameFromUrl(url)), 'wb') as f:
            f.write(file.read())
        print '下载完成: %s'%(os.path.join(save_dir_path,realNameFromUrl(url)))

print '--->共有%s个客户端,已下载完成并保存至路径: \n%s'%(downCount, dir_path)
print '--->当前处理文件夹是: %s \n'%sys.argv[1]

