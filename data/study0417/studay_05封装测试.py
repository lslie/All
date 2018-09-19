from study0417.studa_05封装 import MySql

user = input("请输入用户名：")
password = input("请输入密码:")
db = input("请输入操作的数据库:")

conn = MySql(user,password,db)

conn.open()
#增加
sql = "insert into students(id,name) values(%s,%s)"
params=[0,'宝宝']
conn.make(sql,params)
#删除
sql = "delete from students where id=%s"
params  = [1]
conn.make(sql,params)
#修改
sql = "update students set name=%s where id=%s"
params = ["张旭",5]
conn.make(sql,params)
#查询全部
sql = "select * from students"
params=[]
conn.get_files(sql,params)
#查询一条
sql = "select * from where id=%s"
params=[5]
conn.get_one_files(sql,params)
#增加
sql = "insert into students(id,name) values(%s,%s)"
params=[0,"1902"]
conn.insert(sql,params)
#删除
sql = "delete from students where id=%s"
params  = [9]
conn.delete(sql,params)
#修改
sql = "update students set name=%s where id=%s"
params = ["张旭",5]
conn.update(sql,params)
conn.close()