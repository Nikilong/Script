#!/usr/bin/python
#-*-coding:UTF-8-*-

import urllib2,re

def getUrlRespHtml(url):
    heads = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Charset': 'GB2312,utf-8;q=0.7,*;q=0.7',
             'Accept-Language': 'zh-cn,zh;q=0.5',
             'Cache-Control': 'max-age=0',
             'Connection': 'keep-alive',
             'Host': 'John',
             'Keep-Alive': '115',
             'Referer': url,
             'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.14) Gecko/20110221 Ubuntu/10.10 (maverick) Firefox/3.6.14'}

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    opener.addheaders = heads.items()
    respHtml = opener.open(req).read()
    return respHtml
    # return respHtml.decode('gbk').encode('utf-8')

html = getUrlRespHtml("https://www.javbus2.com/star/n4r")
# print html
print '-----------'
# keyWord = '<div class=\"item\">\\n.*</div>'  #网页链接
# keyWord_arr = re.findall(keyWord,html)
# print keyWord_arr

actor = re.findall('<b>.* - 影片</b>',html)

keyWord_URL = 'href=\"https*://[^\"^)]*[^(\.js)]-\d+\">'  #网页链接
URL_arr = re.findall(keyWord_URL,html)
print URL_arr

keyWord_img_URL = 'src=\"https*://[^\"^)]*[^(\.js)]\.jpg\" title=\".*\">'  #图片
img_URL_arr = re.findall(keyWord_img_URL,html)
print img_URL_arr


print 'url num is %s ; img num is %s' %(len(img_URL_arr),len(URL_arr))

# f = open('/Users/admin/Desktop/log/dong.txt','w')
# for ele in URL_arr:
#     f.write(ele + '\n')
# for ele in img_URL_arr:
#     f.write(ele + '\n')
# f.close()