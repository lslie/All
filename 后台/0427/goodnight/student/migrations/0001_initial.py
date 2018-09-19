# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_grant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='班级', max_length=10)),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': '学生班级',
                'verbose_name': '学生班级',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='学生姓名', max_length=20)),
                ('age', models.IntegerField(verbose_name='学生年龄', default=18)),
                ('gender', models.CharField(default='girl', verbose_name='学生性别', max_length=6, choices=[('girl', '女'), ('boy', '男')])),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=False)),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('th_class', models.ForeignKey(to='student.Class_grant', verbose_name='属于学生的班级')),
            ],
            options={
                'verbose_name_plural': '学生信息',
                'verbose_name': '学生信息',
            },
        ),
        migrations.CreateModel(
            name='StudentId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('stu_no', models.CharField(verbose_name='学号', max_length=20)),
                ('student_no', models.OneToOneField(verbose_name='属于学生的学号', to='student.Student')),
            ],
            options={
                'verbose_name_plural': '学号信息',
                'verbose_name': '学号信息',
            },
        ),
    ]
