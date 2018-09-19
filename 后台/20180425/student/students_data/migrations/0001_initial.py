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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='学生姓名', default='张三')),
                ('age', models.IntegerField(verbose_name='学生年龄', default=18)),
                ('gender', models.CharField(max_length=8, verbose_name='学生性别', choices=[('girl', '女'), ('boy', '男')], default='girl')),
                ('address', models.TextField(verbose_name='学生住址默认为北京', default='北京')),
                ('student_id', models.CharField(max_length=20, verbose_name='学生编号默认为000', default=0)),
                ('height', models.DecimalField(max_digits=5, verbose_name='学生身高默认为170', decimal_places=2, default=170.0)),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
            ],
        ),
    ]
