# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentinfo',
            options={'verbose_name': '学生管理系统', 'verbose_name_plural': '学生管理系统'},
        ),
    ]
