# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='班级')),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': '学生班级',
                'verbose_name': '学生班级',
            },
        ),
        migrations.CreateModel(
            name='StudentId',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('stu_id', models.CharField(max_length=20, verbose_name='学生学号')),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': '学生学号',
                'verbose_name': '学生学号',
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='学生姓名')),
                ('age', models.IntegerField(verbose_name='学生年龄', default=18)),
                ('gender', models.CharField(max_length=6, verbose_name='学生性别', default='girl', choices=[('girl', '女'), ('boy', '男')])),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('th_class', models.ForeignKey(verbose_name='所属班级', to='students.ClassInfo')),
            ],
            options={
                'verbose_name_plural': '学生信息',
                'verbose_name': '学生信息',
            },
        ),
        migrations.AddField(
            model_name='studentid',
            name='th_stu',
            field=models.OneToOneField(verbose_name='所属学号', to='students.StudentInfo'),
        ),
    ]
