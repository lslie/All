from django.db import models

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=20,verbose_name='用户名',unique=True)
    password = models.CharField(max_length=20,verbose_name='用户密码')
    nik_name = models.CharField(max_length=40,verbose_name='用户别称',null=True,blank=True)
    def __str__(self):
        return self.username
    class Meta():
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name