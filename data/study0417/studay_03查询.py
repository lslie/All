import pymysql
#new 对象
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",
    db="python2",
    charset="utf8"
)


#创建执行sql语句对象
cursor = conn.cursor()
name = input("请输入您要查询的姓名")
params = [name]
#str=[]
sql = "select * from students where name=%s"
print(sql)
#执行execute
count = cursor.execute(sql,params)
print(count)
#更新
conn.commit()
#关闭
cursor.close()
conn.close()