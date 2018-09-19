import pymysql

#返回的是链接对象
conn = pymysql.connect(
    host = "127.0.0.1",
    port=3306,
    user="root",
    password="1234",
    db="python2",
    charset="utf8"
)
#得到cursor对象
cursor = conn.cursor()


#执行sql语句
sql = "select * from students"

params=[]

cursor.execute(sql,params)
#得到结果集
all = cursor.fetchall()
for i in all:
    print(i)

#关闭链接
cursor.close()
#关闭对象连接诶
conn.close()