# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(verbose_name='用户名', unique=True, max_length=20)),
                ('password', models.CharField(verbose_name='用户密码', max_length=20)),
                ('nik_name', models.CharField(verbose_name='用户别称', null=True, blank=True, max_length=40)),
            ],
            options={
                'verbose_name_plural': '用户信息',
                'verbose_name': '用户信息',
            },
        ),
    ]
