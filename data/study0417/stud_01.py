import pymysql

#创建对象
conn = pymysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "1234",
    db = "python2",
    charset = "utf8"
)

sql = "insert into students(id,name) values(0,'宝宝')"
# 得到执行sql语句的对象
cursor = conn.cursor()
#使用cursor对象方法excute执行sql语句
cursor.execute(sql)
#更新
conn.commit()
#关闭cursor对象
cursor.close()
#关闭conn对象
conn.close()