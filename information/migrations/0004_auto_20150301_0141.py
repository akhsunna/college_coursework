# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0003_auto_20150225_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicalwork',
            name='kind',
            field=models.CharField(verbose_name='Тип', max_length=255, choices=[('PR', 'Практична'), ('LR', 'Лабораторна')]),
            preserve_default=True,
        ),
    ]
