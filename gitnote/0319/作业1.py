#coding=utf-8
import os
list_num=os.listdir('./')
new_list=[]
for item in list_num:
    a=item.split('.',2)
    #print(a)
    num='py'
    if len(a)==2:
        if a[1]==num:
            new_list.append(a)
for items in new_list:
    print(items)
