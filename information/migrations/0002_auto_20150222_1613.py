# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='practicalwork',
            options={'verbose_name': 'Практично-лабораторна робота', 'verbose_name_plural': 'Практично-лабораторні роботи'},
        ),
        migrations.AlterModelOptions(
            name='practicalworkfile',
            options={'verbose_name': 'Файл до роботи', 'verbose_name_plural': 'Файли до робіт'},
        ),
        migrations.AlterField(
            model_name='checktest',
            name='doc_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Файл'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checktest',
            name='subject',
            field=models.ForeignKey(verbose_name='Предмет', to='information.Subject'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checktest',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Тест'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursenumber',
            name='number',
            field=models.IntegerField(choices=[(1, '1 курс'), (2, '2 курс'), (3, '3 курс'), (4, '4 курс')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lecture',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Тема'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lecture',
            name='number',
            field=models.IntegerField(verbose_name='Номер'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lecture',
            name='subject',
            field=models.ForeignKey(verbose_name='Предмет', to='information.Subject'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicalwork',
            name='kind',
            field=models.IntegerField(choices=[(1, 'Практична'), (2, 'Лабораторна')], verbose_name='Тип'),
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
            name='subject',
            field=models.ForeignKey(verbose_name='Предмет', to='information.Subject'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicalwork',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Тема'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicalworkfile',
            name='document',
            field=models.FileField(upload_to='data/practical_works/', verbose_name='Файл'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicalworkfile',
            name='practical_work',
            field=models.ForeignKey(verbose_name='', to='information.PracticalWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='presentation',
            name='document',
            field=models.FileField(upload_to='data/presentation/', verbose_name='Файл'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='presentation',
            name='lecture',
            field=models.OneToOneField(verbose_name='Лекція', to='information.Lecture'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='presentation',
            name='title',
            field=models.TextField(verbose_name='Тема'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='speciality',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='Повна назва'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='speciality',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Скорочена назва'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Назва'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='specialty',
            field=models.ForeignKey(verbose_name='Спеціальність', to='information.Speciality', related_name='subjects'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='year',
            field=models.ForeignKey(verbose_name='Курс', to='information.CourseNumber'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='theory',
            name='document',
            field=models.FileField(upload_to='data/theory/', verbose_name='Файл'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='theory',
            name='lecture',
            field=models.OneToOneField(verbose_name='Лекція', to='information.Lecture'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='theory',
            name='title',
            field=models.TextField(verbose_name='Тема'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='document',
            field=models.FileField(upload_to='data/video/', verbose_name='Файл'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='lecture',
            field=models.OneToOneField(verbose_name='Лекція', to='information.Lecture'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.TextField(verbose_name='Тема'),
            preserve_default=True,
        ),
    ]
