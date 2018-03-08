#!/usr/bin/env python
#coding:utf-8

import urllib2
import threading
import time
import sys,urllib


def test():
    print '线程1回调'

def test2():
    print '线程2回调'

def sel():
    print 'sel run'
    img = urllib2.urlopen("http://wx2.sinaimg.cn/mw690/3fb4c2e1gy1fj5oluxiqfg20fk08rx75.gif")
    print '-----'
    content=dict(img.headers)['content-length']
    print 'content-length:%s'%content
#    print len(img.read())
#    with open ('/Users/admin/Desktop/test/test.gif','wb') as f:
#        f.write(img.read())

def sel2():
    print 'sel2 run'
    img = urllib2.urlopen("http://wx2.sinaimg.cn/mw690/3fb4c2e1gy1fj5oluxiqfg20fk08rx75.gif")
    with open ('/Users/admin/Desktop/test/test2.gif','wb') as f:
        f.write(img.read())

class WorkerThread(threading.Thread):
    
    def __init__(self, callback, target):
        super(WorkerThread, self).__init__()
        self.callback = callback
        self.target = target

    
    def run(self):
        self.target()
        self.callback()

#thread = WorkerThread(target=sel,callback=test)
#thread.start()

#thread2 = WorkerThread(target=sel2,callback=test2)
#thread2.start()



def report(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r ....已下载: %d%%" % percent)
    sys.stdout.flush()


getFile='http://wx2.sinaimg.cn/mw690/3fb4c2e1gy1fj5oluxiqfg20fk08rx75.gif'
saveFile='/Users/admin/Desktop/test/test2.gif'

sys.stdout.write('\r正在下载: ' + saveFile + '...\n')
urllib.urlretrieve(getFile, saveFile, reporthook=report)
sys.stdout.write("\r下载完成, 保存到 %s" % (saveFile) + '\n\n')
sys.stdout.flush()
