#!/usr/bin/python
#coding:UTF-8

import os,re,sys,urllib2,urllib,ssl,time

#全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context
# 获取网页源代码
def getUrlRespHtml(url):
    # 要设置请求头，让服务器知道不是机器人
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    
    request = urllib2.Request(url, headers=headers)
    #尝试去获取网页源代码
    try:
        #等待时间20秒
        html = urllib2.urlopen(request,timeout=20)
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

#1.分析url
maspApp_url = sys.argv[1]
#拼接masp/app
if not 'masp/app' in maspApp_url:
    if maspApp_url[-1] == '/':
        maspApp_url = '%smasp/app'%maspApp_url
    else:
        maspApp_url = '%s/masp/app'%maspApp_url

#拼接http/https
if not 'http' in maspApp_url:
    temp_url = 'http://%s'%maspApp_url
    
    print '--->尝试连接 %s ....'%temp_url
    if getUrlRespHtml(temp_url) == None:
        temp_url = 'https://%s'%maspApp_url
        print '尝试连接 %s ....'%temp_url
        if getUrlRespHtml(temp_url) == None:
            print '!!!!输入的URL无效 \n*********结束*********'
            exit(0)
        maspApp_url = temp_url
    else:
        maspApp_url = temp_url

print '--->拼接后的MASP/APP的有效URL为: %s'%maspApp_url


#2.通过支撑平台下载页面来下载客户端
#html = getUrlRespHtml('https://iexoa.nbport.com.cn/masp/app/applist.jsp')
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
        print '!!!!无法从%s获得内容 \n*******结束*******'%maspApp_url
        exit(0)
else:
    print '!!!!无法从%s获得内容 \n*******结束*******'%maspApp_url
    exit(0)

# 获得时间戳 03-06_10:07拼接文件路径,url是证明从网址下载的客户端
timeStr = time.strftime('%m-%d_%H:%M',time.localtime())
dir_path = '/Users/Longcq/Downloads/jenkins下载/url_%s'%(timeStr)

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
print '--->当前URL是: %s \n'%maspApp_url




##"https://172.20.105.92/masp/clientProgram/edit.do?id=ff8080816168b8460161691e26c60105"这样拼接可以进入支撑平台的客户端列表并拿到客户端的信息,但是必须要登录
