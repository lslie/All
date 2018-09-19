#host = "127.0.0.1"

help = MySqlHelp()
sql = "select * from students"
param=[]
help.get_all(sql)
# for i in all:
#     print(i)