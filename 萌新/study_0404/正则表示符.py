# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 正则表示符.py 18-4-4 下午2:29
# SITE: https:www.jetbrains.com/pycharm/
import re

# .表示任意字符匹配[	]中列举的字符
obj = re.match("[w]\w\w\W\S\S\S\S\S\W\D\D\D\s", "www.baidu.com ")
if obj != None:
    print(obj.group())
else:
    print("没有")
if __name__ == "__main__":
    pass
