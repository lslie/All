from django.db import models
from datetime import datetime

# Create your models here.

class UserProFile(models.Model):
    username = models.CharField(max_length=20,verbose_name='账户名称',unique=True)
    password = models.CharField(max_length=20,verbose_name='账户密码')
    nik_name = models.CharField(max_length=20,verbose_name='账户昵称')
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    def __str__(self):
        return self.username
    class Meta():
        verbose_name = '账户信息'
        verbose_name_plural = verbose_name