import pymysql
class MySql1(object):
    #默认
    def __init__(self,user,password,db):
        self.host = "localhost"
        self.port = 3306
        self.user = user
        self.password = password
        self.db = db
        self.charset = "utf8"

    #创建对象
    def open(self):
        self.conn = pymysql.connect(
            host = "localhost",
            port = 3306,
            user = self.user,
            password = self.password,
            db = self.db,
            charset = "utf8",
        )

        #创建执行sql语句
        self.cursor = self.conn.cursor()

    #关闭
    def close(self):
        self.cursor.close()
        self.conn.close()
    #增加和删除
    def make(self,sql,params=[]):
        try:
            self.open()
            self.cursor.execute(sql, params)
            self.conn.commit()
            self.cursor.close()
            print("over")
        except Exception as a:
            print(a)

    #获取全部数据
    def get_files(self,sql,params=[]):
        try:
            self.open()
            self.cursor.execute(sql,params)
            all = self.cursor.fetchall()
            self.cursor.close()
            return all
        except Exception as a:
            print(a)

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

    #增加
    def insert(self,sql,params=[]):
        self.__hide(sql,params)

    #删除
    def delete(self,sql,params=[]):
        self.__hide(sql,params)
    #修改
    def update(self,sql,params=[]):
        self.__hide(sql,params)
    #修改数据
    def __hide(self,sql,params=[]):
        try:
            self.open()
            self.cursor.execute(sql, params)
            self.conn.commit()
            self.cursor.close()
            print("over")
        except Exception as a:
            print(a)