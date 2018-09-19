# coding=utf-8
# Copyright 2018 XXX. All Right Reserved
# Author: test@XXX.com{test}
# 文件操作.py 18-4-10 下午9:06
# SITE: https:www.jetbrains.com/pycharm/


if __name__ == "__main__":
    f = open("haha.txt","r")
    #f.write("1234567")
    print(f.tell())
    f.seek(3,0)

    print(f.tell())
    a = f.readlines()
    print(a)
    f.close()
