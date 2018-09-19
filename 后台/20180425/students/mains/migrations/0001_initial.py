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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='学生姓名')),
                ('age', models.IntegerField(default=18, verbose_name='学生年龄')),
                ('gender', models.CharField(default='girl', verbose_name='学生性别', choices=[('girl', '女'), ('boy', '男')], max_length=6)),
                ('stuid', models.CharField(max_length=20, verbose_name='学生学号')),
                ('address', models.TextField(verbose_name='学生地址')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name_plural': '学生信息',
                'verbose_name': '学生信息',
            },
        ),
    ]
