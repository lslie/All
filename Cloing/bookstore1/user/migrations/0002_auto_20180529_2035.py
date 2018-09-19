# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='is_delete',
            field=models.BooleanField(verbose_name='是否删除', default=False),
        ),
    ]
