from django.db import models
#from django.contrib.auth.models import AbstractUser,User
from datetime import datetime

# Create your models here.

class UserProfile(models.Model):
    nick_name = models.CharField(max_length=20,verbose_name='用户别称')
    user_email = models.EmailField(verbose_name='用户邮箱')
    user_title = models.CharField(max_length=50,verbose_name='留言主题')
    user_content = models.TextField(verbose_name='留言内容')
    add_time = models.DateField(default=datetime.now,verbose_name='增加时间')
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')

    def __str__(self):
        return self.nick_name

    class Meta():
        verbose_name = '留言用户信息'
        verbose_name_plural = verbose_name
