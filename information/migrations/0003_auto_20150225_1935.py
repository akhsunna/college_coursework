# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('information', '0002_auto_20150222_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecture',
            options={'verbose_name': 'Лекція', 'verbose_name_plural': 'Лекції'},
        ),
        migrations.AlterModelOptions(
            name='presentation',
            options={'verbose_name': 'Презентація', 'verbose_name_plural': 'Презентації'},
        ),
        migrations.AlterModelOptions(
            name='theory',
            options={'verbose_name': 'Теорія', 'verbose_name_plural': 'Теорії'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Відеофайл', 'verbose_name_plural': 'Відеофайли'},
        ),
        migrations.AddField(
            model_name='subject',
            name='author',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
