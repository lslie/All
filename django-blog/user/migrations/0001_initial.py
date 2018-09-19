# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nick_name', models.CharField(verbose_name='用户别称', max_length=20)),
                ('user_email', models.EmailField(verbose_name='用户邮箱', max_length=254)),
                ('user_title', models.CharField(verbose_name='留言主题', max_length=50)),
                ('user_content', models.TextField(verbose_name='留言内容')),
                ('add_time', models.DateField(verbose_name='增加时间', default=datetime.datetime.now)),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=False)),
            ],
            options={
                'verbose_name': '留言用户信息',
                'verbose_name_plural': '留言用户信息',
            },
        ),
    ]
