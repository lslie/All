#! /usr/local/bin python
# ! -*-coding:utf-8 -*-
# ! time      :9/25/18 15:00
# ! @Auther   : whitek
# ! @File     :model.py
# ! code is far away from bugs with the god animal protecting i love animals.They taste delicious.

import web
import datetime

# 连接数据库
db = web.database(dbn='mysql', db = 'entries', user = 'root', pw = '1234')

# 获取所有文章
def get_posts():
    return db.select('entries', order='id DESC')

# 获取文章内容
def get_post(id):
    try:
        return db.select('entries', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

# 新建文章
def new_post(title, text):
    db.insert('entries', title=title, content=text, posted_on=datetime.datetime.now())

# 删除文章
def del_post(id):
    db.delete('entries', where='id=$id', vars=locals())

# 修改文章
def update_post(id, title, text):
    db.update('entries', where='id=$id', vars=locals(), title=title, content=text)
