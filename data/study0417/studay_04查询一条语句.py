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


cursor = conn.cursor()
params=[]
sql = "select * from students"
cursor.execute(sql)
# all=cursor.fetchall()
one = cursor.fetchone()
for i in one:
    print(i)

conn.commit()
cursor.close()
conn.close()