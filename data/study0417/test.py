from study0417 import py_链接数据库

# 返回Connection对象
# host="localhost"
con = py_链接数据库.connect(host="192.168.31.28",
                       port=3306, user="atguigu",
                       password="atguigu",
                       db="atguigudb",
                       charset="utf8")
# 返回cursor对象
cursor = con.cursor()
# SQL语言-SQL语句
sql = "insert into students(name) value('李四')"
# 插入数据
cursor.execute(sql)
# 提交数据,没有提交就没有数据
con.commit()
# 关闭释放资源
cursor.close()
# 关闭资源
con.close()
