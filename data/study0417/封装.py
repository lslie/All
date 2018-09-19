import pymysql
try:
   conn=pymysql.connect(
      host='localhost',
      port=3306,
      db='python2',
      user='root',
      passwd='1234',
      charset='utf8'
   )
   cursor=conn.cursor()
   cname=input("请输入学生姓名：")
   params=[cname]
   # count=cs1.execute('insert into students(name) values(%s)',params)
   count = cursor.execute('select * from students where name = %s', params)
   print("count=",count)
   conn.commit()
   cursor.close()
   conn.close()
except Exception as e:
   print(e.message)
