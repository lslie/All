# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProFile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(unique=True, max_length=20, verbose_name='账户名称')),
                ('message', models.CharField(max_length=20, verbose_name='账户密码')),
                ('nik_name', models.CharField(max_length=20, verbose_name='账户昵称')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '账户信息',
                'verbose_name': '账户信息',
            },
        ),
    ]
