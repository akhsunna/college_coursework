# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckTest',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тест')),
                ('doc_name', models.FileField(upload_to='data/test/', verbose_name='Файл')),
            ],
            options={
                'verbose_name_plural': 'Підсумкові',
                'verbose_name': 'Підсумкок',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseNumber',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(choices=[(1, '1 курс'), (2, '2 курс'), (3, '3 курс'), (4, '4 курс')])),
            ],
            options={
                'verbose_name_plural': 'Курси',
                'verbose_name': 'Курс',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('name', models.CharField(max_length=255, verbose_name='Тема')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Лекції',
                'verbose_name': 'Лекція',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PracticalWork',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=255, choices=[('PR', 'Практична'), ('LR', 'Лабораторна')], verbose_name='Тип')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('title', models.CharField(max_length=255, verbose_name='Тема')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Практично-лабораторні роботи',
                'verbose_name': 'Практично-лабораторна робота',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PracticalWorkFile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='data/practical_works/', verbose_name='Файл')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('practical_work', models.ForeignKey(to='information.PracticalWork', verbose_name='')),
            ],
            options={
                'verbose_name_plural': 'Файли до робіт',
                'verbose_name': 'Файл до роботи',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Опис')),
                ('document', models.FileField(upload_to='data/presentationn/', verbose_name='Файл')),
                ('lecture', models.OneToOneField(to='information.Lecture', verbose_name='Лекція')),
            ],
            options={
                'verbose_name_plural': 'Презентації',
                'verbose_name': 'Презентація',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Скорочена назва')),
                ('full_name', models.CharField(max_length=255, verbose_name='Повна назва')),
            ],
            options={
                'verbose_name_plural': 'Спеціальності',
                'verbose_name': 'Спеціальність',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('specialty', models.ForeignKey(to='information.Speciality', related_name='subjects', verbose_name='Спеціальність')),
                ('year', models.ForeignKey(to='information.CourseNumber', verbose_name='Курс')),
            ],
            options={
                'verbose_name_plural': 'Предмети',
                'verbose_name': 'Предмет',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Опис')),
                ('document', models.FileField(upload_to='data/theory/', verbose_name='Файл')),
                ('lecture', models.OneToOneField(to='information.Lecture', verbose_name='Лекція')),
            ],
            options={
                'verbose_name_plural': 'Теорії',
                'verbose_name': 'Теорія',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Опис')),
                ('document', models.FileField(upload_to='data/video/', verbose_name='Файл')),
                ('lecture', models.OneToOneField(to='information.Lecture', verbose_name='Лекція')),
            ],
            options={
                'verbose_name_plural': 'Відеофайли',
                'verbose_name': 'Відеофайл',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='practicalwork',
            name='subject',
            field=models.ForeignKey(to='information.Subject', verbose_name='Предмет'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lecture',
            name='subject',
            field=models.ForeignKey(to='information.Subject', verbose_name='Предмет'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='checktest',
            name='subject',
            field=models.ForeignKey(to='information.Subject', verbose_name='Предмет'),
            preserve_default=True,
        ),
    ]
