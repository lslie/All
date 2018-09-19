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


#创建执行sql语句cursor对象
cursor = conn.cursor()

sql = "delete from students where id=21"

#调用cursor的方法 execute
cursor.execute(sql)

#更新
conn.commit()
#关闭
cursor.close()
conn.close()