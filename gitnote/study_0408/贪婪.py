# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 贪婪.py 18-4-8 下午2:03
# SITE: https:www.jetbrains.com/pycharm/
import re

if __name__ == "__main__":
    # content = "This is a number 234-789-567-3456"
    #
    # sun = re.match(r"(.+?)(\d+-\d+-\d+-\d+)",content)
    # print(sun)
    # print(sun.group(1))
    # print(sun.group(2))
    # html = '''<img src="https://rpic.douyucdn.cn/amrpic-180408/84452_1413.jpg"
    # data-original="https://rpic.douyucdn.cn/amrpic-180408/84452_1416.jpg"
    # style="display: block;">'''
    #
    # sun = re.findall(r"https://.+?\.jpg",html)
    # print(sun)
    list1=[
        "http://www.interoem.com/messageinfo.asp?id = 35",
        "http://3995503.com/class/class09/news_show.asp?id=14",
        "http://lib.wzmc.edu.cn/news/onews.asp?id = 769",
        "http://www.zy-ls.com/alfx.asp?newsid = 377 & id = 6",
        "http://www.fincm.com/newslist.asp?id = 415"
    ]
    list2 = []
    for str in list1:
        str1 = re.search(r"http://.+?/",str)
        print(str1.group())