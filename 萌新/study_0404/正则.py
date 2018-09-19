# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 正则.py 18-4-4 下午2:18
# SITE: https:www.jetbrains.com/pycharm/
import re
def main():
    #pattern 表示正则表达式
    re_obj = re.match("aa","aabcsaadfd")
    print(type(re_obj),re_obj)
    #如果匹配成功的话，返回一个该SRE_Match类型对象
    # 此对象中包含位置span=(), 匹配的元素match=''
if __name__ == "__main__":
    main()