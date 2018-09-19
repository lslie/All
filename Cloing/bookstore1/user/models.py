from django.db import models
from db.base_model import BaseModel
from utils.get_hash import get_hash

# Create your models here.
# class Passport(BaseModel):
#     '''用户模型类'''
#     username = models.CharField(max_length=20, unique=True, verbose_name='用户名称')
#     password = models.CharField(max_length=40, verbose_name='用户密码')
#     email = models.EmailField(verbose_name='用户邮箱')
#     is_active = models.BooleanField(default=False, verbose_name='激活状态')
#
#     class Meta():
#         db_table = 's_user_accoumt'
# 实现用户的添加和查找账户信息的功能
class PassportManager(models.Manager):

    def add_user(self,username, password, email):
        '''添加一个用户信息'''
        passport = self.create(username=username, password=get_hash(password), email=email)

        # 并且返回当前的数据
        return passport

    def find_user(self,username, password):
        '''根据用户的信息进行查找用户'''
        try:
            passport = self.get(username=username, password=get_hash(password))
        except self.model.DoesNotExist:
            # 账户不存在
            print("=======")
            passport = None
        # 返回当前的信息
        return passport
class Passport(BaseModel):
    username = models.CharField(max_length=20,verbose_name='用户名称',unique=True)
    password = models.CharField(max_length=40,verbose_name='用户密码')
    email = models.EmailField(verbose_name='用户邮箱')
    is_active = models.BooleanField(default=False, verbose_name='激活状态')

    def __str__(self):
        return self.username
    # 创建用户表的管理器
    object = PassportManager()

    class Meta():
        # 指定数据库名称
        db_table = 's_user_accoumt'