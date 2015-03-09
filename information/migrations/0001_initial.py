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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Тест', max_length=255)),
                ('doc_name', models.CharField(verbose_name='Файл', blank=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('number', models.IntegerField(choices=[(1, '1 курс'), (2, '2 курс'), (3, '3 курс'), (4, '4 курс')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('name', models.CharField(verbose_name='Тема', max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Лекція',
                'verbose_name_plural': 'Лекції',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PracticalWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('kind', models.CharField(verbose_name='Тип', max_length=255, choices=[('PR', 'Практична'), ('LR', 'Лабораторна')])),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('title', models.CharField(verbose_name='Тема', max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Практично-лабораторна робота',
                'verbose_name_plural': 'Практично-лабораторні роботи',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PracticalWorkFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('document', models.FileField(verbose_name='Файл', upload_to='data/practical_works/', blank=True)),
                ('practical_work', models.ForeignKey(verbose_name='', to='information.PracticalWork')),
            ],
            options={
                'verbose_name': 'Файл до роботи',
                'verbose_name_plural': 'Файли до робіт',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.TextField(verbose_name='Тема')),
                ('document', models.FileField(verbose_name='Файл', upload_to='data/presentation/')),
                ('lecture', models.OneToOneField(verbose_name='Лекція', to='information.Lecture')),
            ],
            options={
                'verbose_name': 'Презентація',
                'verbose_name_plural': 'Презентації',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Скорочена назва', max_length=255)),
                ('full_name', models.CharField(verbose_name='Повна назва', max_length=255)),
            ],
            options={
                'verbose_name': 'Спеціальність',
                'verbose_name_plural': 'Спеціальності',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Назва', max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('specialty', models.ForeignKey(to='information.Speciality', verbose_name='Спеціальність', related_name='subjects')),
                ('year', models.ForeignKey(verbose_name='Курс', to='information.CourseNumber')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предмети',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.TextField(verbose_name='Тема')),
                ('document', models.FileField(verbose_name='Файл', upload_to='data/theory/')),
                ('lecture', models.OneToOneField(verbose_name='Лекція', to='information.Lecture')),
            ],
            options={
                'verbose_name': 'Теорія',
                'verbose_name_plural': 'Теорії',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.TextField(verbose_name='Тема')),
                ('document', models.FileField(verbose_name='Файл', upload_to='data/video/')),
                ('lecture', models.OneToOneField(verbose_name='Лекція', to='information.Lecture')),
            ],
            options={
                'verbose_name': 'Відеофайл',
                'verbose_name_plural': 'Відеофайли',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='practicalwork',
            name='subject',
            field=models.ForeignKey(verbose_name='Предмет', to='information.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lecture',
            name='subject',
            field=models.ForeignKey(verbose_name='Предмет', to='information.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='checktest',
            name='subject',
            field=models.ForeignKey(verbose_name='Предмет', to='information.Subject'),
            preserve_default=True,
        ),
    ]
