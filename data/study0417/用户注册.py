from study0417.studay_06用户登录 import Mysql

import hashlib
import re


conn = Mysql()
username = input("用户名:")
password = input("密码:")
password = hashlib.sha1(password.encode("utf-8")).hexdigest()
print(password)
sql="select %s,%s from new_user"
params = [username, password]
count= conn.get_all(sql,params)
print(count)
if count[0]==username and count[1]==password:
    print("登录成功")
else:
    print("登录失败")