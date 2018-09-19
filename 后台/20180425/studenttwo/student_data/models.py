from django.db import models
from datetime import datetime

# Create your models here.
class StudentInfo(models.Model):
    name = models.CharField(max_length=10,verbose_name='学生姓名',default='张三')
    age = models.IntegerField(default=18,verbose_name='学生年龄')
    gender = models.CharField(choices=(('girl','女'),('boy','男')),default='girl',max_length=6,verbose_name='学生性别')
    class_college = models.CharField(max_length=30,verbose_name='学生学院信息')
    we_cat = models.CharField(max_length=30,default='0000000',verbose_name='微信号')
    address = models.TextField(default='无',verbose_name='学生联系地址')
    #image = models.ImageField(upload_to='user/%y/%m/%d',verbose_name='学生头像')
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    def __str__(self):
        return self.name

    class Meta():
        verbose_name = '学生管理系统'
        verbose_name_plural = verbose_name