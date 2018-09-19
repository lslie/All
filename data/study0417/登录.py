from study0417.studay_06用户登录 import Mysql

import hashlib
import re

conn = Mysql()
username = input("请输入您想注册的用户名:")
password = input("请输入注册密码:")
password = hashlib.sha1(password.encode("utf-8")).hexdigest()
print(password)
sql="select uname,upwd from userinfos where uname=%s"
#sql = "select "
params=[username]
str = conn.get_one_files(sql,params)
print(str)
if str[0]==username and str[1] == password:
    print("登陆成功")
else:
    print("用户名或者密码错误!")
conn.close()
#登录
