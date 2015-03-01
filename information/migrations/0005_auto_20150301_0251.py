# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0004_auto_20150301_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicalwork',
            name='kind',
            field=models.CharField(blank=True, verbose_name='Тип', max_length=255, choices=[('PR', 'Практична'), ('LR', 'Лабораторна')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicalwork',
            name='number',
            field=models.IntegerField(blank=True, verbose_name='Номер'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicalwork',
            name='title',
            field=models.CharField(blank=True, verbose_name='Тема', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicalworkfile',
            name='document',
            field=models.FileField(blank=True, verbose_name='Файл', upload_to='data/practical_works/'),
            preserve_default=True,
        ),
    ]
