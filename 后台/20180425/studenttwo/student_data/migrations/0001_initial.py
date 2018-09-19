# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='学生姓名', default='张三')),
                ('age', models.IntegerField(verbose_name='学生年龄', default=18)),
                ('gender', models.CharField(max_length=6, verbose_name='学生性别', default='girl', choices=[('girl', '女'), ('boy', '男')])),
                ('class_college', models.CharField(verbose_name='学生学院信息', max_length=30)),
                ('we_cat', models.CharField(max_length=30, verbose_name='微信号', default='0000000')),
                ('address', models.TextField(verbose_name='学生联系地址', default='无')),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=False)),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '学生管理系统',
                'verbose_name_plural': '学生管理系统',
            },
        ),
    ]
