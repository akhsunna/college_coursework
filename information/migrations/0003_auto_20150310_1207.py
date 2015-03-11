# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_auto_20150309_2117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursenumber',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курси'},
        ),
        migrations.AlterField(
            model_name='checktest',
            name='doc_name',
            field=models.FileField(verbose_name='Файл', upload_to='data/test/'),
            preserve_default=True,
        ),
    ]
