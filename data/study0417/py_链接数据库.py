#倒库
import pymysql

conn =pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="1234",
    db="python2",
    charset="utf8"
)
#返回一个cursor对象
cursor = conn.cursor()

#sql = "create database html charset=utf8"
#使用sql语句
sql = "insert into students(id,name) values(0,'张旭')"

cursor.execute(sql)

conn.commit()
cursor.close()
conn.close()