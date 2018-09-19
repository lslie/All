import pymysql
import hashlib


class Mysql(object):
    def __init__(self):
        self.host = "localhost"
        self.port = 3306
        self.user = "root"
        self.password = "1234"
        self.db = "python2"
        self.charset = "utf8"

    def open(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.charset
        )
        # 执行sql语句
        self.cursor = self.conn.cursor()

    # 创建用户表
    def create_user(self):
        self.open()
        sql = '''create table new_user(id int primary key auto_increment not null,username varchar(20) unique,userpwd char(45),isdelete bit default 0)charset=utf8;'''
        self.cursor.execute(sql)
        print("创建成功")

    #关闭
    def create_users(self,sql,params=[]):
        try:
            self.open()
            self.cursor.execute(sql,params)
            self.conn.commit()
            self.cursor.close()
            print("创建成功！")
            return 1
        except Exception as a:
            return None

        # 获取一条数据
    def get_one_files(self, sql, params=[]):
        try:
            self.open()
            self.cursor.execute(sql, params)
            one = self.cursor.fetchone()
            self.cursor.close()
            return one
        except Exception as a:
            print(a)

    def get_all(self,sql,params=[]):
        try:
            self.open()
            self.cursor.execute(sql,params)
            return self.cursor.fetchone()
        except Exception as e:
            print(e)
    def close(self):
        self.cursor.close()
        self.conn.close()