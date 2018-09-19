from django.db import models
from datetime import datetime


# Create your models here.


# 班级，学生，学号

class Class_grade(models.Model):
    name = models.CharField(max_length=10, verbose_name='班级')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = '班级'
        verbose_name_plural = verbose_name


class Student(models.Model):
    name = models.CharField(max_length=10, verbose_name='学生姓名')
    age = models.IntegerField(default=18, verbose_name='学生年龄')
    gender = models.CharField(choices=(('girl', '女'), ('boy', '男')), default='girl', max_length=6, verbose_name='学生性别')
    # 所属班级
    th_class = models.ForeignKey(Class_grade, verbose_name='所属班级')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name


class Student_Id(models.Model):
    student_no = models.CharField(max_length=20, verbose_name='学号')
    th_student = models.OneToOneField(Student, verbose_name='所属学生')

    def __str__(self):
        return self.student_no

    class Meta():
        verbose_name = '学生学号'
        verbose_name_plural = verbose_name
