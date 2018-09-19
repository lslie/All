# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='文章标题')),
                ('desc', models.CharField(max_length=200, verbose_name='文章摘要')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('click_num', models.IntegerField(default=0, verbose_name='浏览量')),
                ('love_num', models.IntegerField(default=0, verbose_name='点赞数')),
                ('image', models.ImageField(max_length=200, upload_to='article/%y/%m/%d', verbose_name='文章图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='文章作者')),
            ],
            options={
                'verbose_name_plural': '文章信息',
                'verbose_name': '文章信息',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='文章类别')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '文章类别',
                'verbose_name': '文章类别',
            },
        ),
        migrations.CreateModel(
            name='TagInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('article', models.ManyToManyField(to='articles.ArticleInfo', verbose_name='文章标签')),
            ],
            options={
                'verbose_name_plural': '文章标签',
                'verbose_name': '文章标签',
            },
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='label',
            field=models.ForeignKey(null=True, blank=True, verbose_name='文章类别', to='articles.Category'),
        ),
    ]
