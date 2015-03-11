# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='title',
            field=models.TextField(verbose_name='Опис'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='theory',
            name='title',
            field=models.TextField(verbose_name='Опис'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.TextField(verbose_name='Опис'),
            preserve_default=True,
        ),
    ]
