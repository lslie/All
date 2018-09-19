from django.db import models
from datetime import datetime

# Create your models here.
class ClassInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name='班级')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    def __str__(self):
        return self.name
    class Meta():
        verbose_name = '学生班级'
        verbose_name_plural = verbose_name


class StudentInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name='学生姓名')
    age = models.IntegerField(default=18,verbose_name='学生年龄')
    gender = models.CharField(choices=(('girl','女'),('boy','男')),max_length=6,default='girl',verbose_name='学生性别')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    th_class = models.ForeignKey(ClassInfo,verbose_name='所属班级')
    def __str__(self):
        return self.name
    class Meta():
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name

class StudentId(models.Model):
    stu_id = models.CharField(max_length=20,verbose_name='学生学号')
    th_stu = models.OneToOneField(StudentInfo,verbose_name='所属学号')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    def __str__(self):
        return self.stu_id
    class Meta():
        verbose_name = '学生学号'
        verbose_name_plural = verbose_name