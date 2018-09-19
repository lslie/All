# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# urllib_request.py 18-4-9 下午7:00
# SITE: https:www.jetbrains.com/pycharm/
from gevent import monkey
monkey.patch_all()
import gevent
import urllib.request


#下载地址
def my_download(url):
   print("GET url==%s" % url)
   result = urllib.request.urlopen(url)
   data = result.read()
   print("url==%s,data is len=%s" % (url,len(data)))


gevent.joinall([
gevent.spawn(my_download,"https://www.baidu.com"),
gevent.spawn(my_download,"http://www.atguigu.com"),
gevent.spawn(my_download,"https://github.com"),
gevent.spawn(my_download,"http://www.atguigu.com/images/logo.gif"),

])

