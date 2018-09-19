# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='班级', max_length=10)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '班级',
                'verbose_name': '班级',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='学生姓名', max_length=10)),
                ('age', models.IntegerField(default=18, verbose_name='学生年龄')),
                ('gender', models.CharField(default='girl', choices=[('girl', '女'), ('boy', '男')], verbose_name='学生性别', max_length=6)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('th_class', models.ForeignKey(to='user.Class_grade', verbose_name='所属班级')),
            ],
            options={
                'verbose_name_plural': '学生信息',
                'verbose_name': '学生信息',
            },
        ),
        migrations.CreateModel(
            name='Student_Id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('student_no', models.CharField(verbose_name='学号', max_length=20)),
                ('th_student', models.OneToOneField(to='user.Student', verbose_name='所属学生')),
            ],
            options={
                'verbose_name_plural': '学生学号',
                'verbose_name': '学生学号',
            },
        ),
    ]
