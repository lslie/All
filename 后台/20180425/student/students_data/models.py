from django.db import models
from datetime import datetime

# Create your models here.



class StudentInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name='学生姓名',default='张三')
    age = models.IntegerField(default=18,verbose_name='学生年龄')
    gender = models.CharField(choices=(('girl','女'),('boy','男')),default='girl',max_length=8,verbose_name='学生性别')
    address = models.TextField(verbose_name='学生住址默认为北京',default='北京')
    student_id = models.CharField(max_length=20,verbose_name='学生编号默认为000',default=000)
    height = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='学生身高默认为170',default=170.00)
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    #image = models.ImageField(upload_to='user/%y/%m/%d',max_length=100,verbose_name='学生头像',default=None)
    def  __str__(self):
        return self.name
    class Meta():
        verbose_name = '学生管理系统'
        verbose_name_plural = verbose_name