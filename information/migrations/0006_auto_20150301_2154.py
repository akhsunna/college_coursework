# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0005_auto_20150301_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicalwork',
            name='kind',
            field=models.CharField(choices=[('PR', 'Практична'), ('LR', 'Лабораторна')], max_length=255, verbose_name='Тип'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicalwork',
            name='number',
            field=models.IntegerField(verbose_name='Номер'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicalwork',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Тема'),
            preserve_default=True,
        ),
    ]
