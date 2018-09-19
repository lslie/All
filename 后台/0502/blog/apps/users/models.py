from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
'''
AbstractUser是专门用来让用户模块继承的类里面内置了username字段
我们可以添加自己需要的字段来进行开发
'''
# Create your models here.
class UserProFile(AbstractUser):
    nik_name = models.CharField(max_length=20,verbose_name='用户昵称',null=True,blank=True)
    url = models.URLField(max_length=100,verbose_name='用户主页',null=True,blank=True)
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')
    def __str__(self):
        return self.username
    class Meta():
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name