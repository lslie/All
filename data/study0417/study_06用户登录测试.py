from study0417.studay_06用户登录 import Mysql

import hashlib
import re


conn = Mysql()

#conn.create_user()
#创建用户
username = input("请输入您想注册的用户名:")
try:
    count = re.match("\w{4,20}",username)
    username = count.group()
    password = input("请输入注册密码:")
    password = hashlib.sha1(password.encode("utf-8")).hexdigest()
    print(password)
    sql="insert into new_user values(0,%s,%s,0)"
    #sql="select uname,upwd from userinfos where uname=%s"
    #sql = "select "
    params = [username,password]
    a = conn.create_users(sql,params)
    if a == 1:
        print("注册成功")
    else:
        print("注册失败")
    conn.close()
except Exception as a:
    print("用户名长度不正确")