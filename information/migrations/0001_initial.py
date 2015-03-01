# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'\xd0\xa2\xd0\xb5\xd1\x81\xd1\x82')),
                ('doc_name', models.CharField(max_length=255, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(choices=[(1, b'1 \xd0\xba\xd1\x83\xd1\x80\xd1\x81'), (2, b'2 \xd0\xba\xd1\x83\xd1\x80\xd1\x81'), (3, b'3 \xd0\xba\xd1\x83\xd1\x80\xd1\x81'), (4, b'4 \xd0\xba\xd1\x83\xd1\x80\xd1\x81')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80')),
                ('name', models.CharField(max_length=255, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u041b\u0435\u043a\u0446\u0456\u044f',
                'verbose_name_plural': '\u041b\u0435\u043a\u0446\u0456\u0457',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PracticalWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.IntegerField(verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf', choices=[(1, b'\xd0\x9f\xd1\x80\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x87\xd0\xbd\xd0\xb0'), (2, b'\xd0\x9b\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80\xd0\xbd\xd0\xb0')])),
                ('number', models.IntegerField(verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80')),
                ('title', models.CharField(max_length=255, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0430\u043a\u0442\u0438\u0447\u043d\u043e-\u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430 \u0440\u043e\u0431\u043e\u0442\u0430',
                'verbose_name_plural': '\u041f\u0440\u0430\u043a\u0442\u0438\u0447\u043d\u043e-\u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0456 \u0440\u043e\u0431\u043e\u0442\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PracticalWorkFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document', models.FileField(upload_to=b'data/practical_works/', verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb')),
                ('name', models.CharField(max_length=255, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0')),
                ('practical_work', models.ForeignKey(verbose_name=b'', to='information.PracticalWork')),
            ],
            options={
                'verbose_name': '\u0424\u0430\u0439\u043b \u0434\u043e \u0440\u043e\u0431\u043e\u0442\u0438',
                'verbose_name_plural': '\u0424\u0430\u0439\u043b\u0438 \u0434\u043e \u0440\u043e\u0431\u0456\u0442',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0')),
                ('document', models.FileField(upload_to=b'data/presentation/', verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb')),
                ('lecture', models.OneToOneField(verbose_name=b'\xd0\x9b\xd0\xb5\xd0\xba\xd1\x86\xd1\x96\xd1\x8f', to='information.Lecture')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0435\u0437\u0435\u043d\u0442\u0430\u0446\u0456\u044f',
                'verbose_name_plural': '\u041f\u0440\u0435\u0437\u0435\u043d\u0442\u0430\u0446\u0456\u0457',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xd0\xa1\xd0\xba\xd0\xbe\xd1\x80\xd0\xbe\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0')),
                ('full_name', models.CharField(max_length=255, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb2\xd0\xbd\xd0\xb0 \xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0')),
            ],
            options={
                'verbose_name': '\u0421\u043f\u0435\u0446\u0456\u0430\u043b\u044c\u043d\u0456\u0441\u0442\u044c',
                'verbose_name_plural': '\u0421\u043f\u0435\u0446\u0456\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0456',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('specialty', models.ForeignKey(related_name='subjects', verbose_name=b'\xd0\xa1\xd0\xbf\xd0\xb5\xd1\x86\xd1\x96\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x96\xd1\x81\xd1\x82\xd1\x8c', to='information.Speciality')),
                ('year', models.ForeignKey(verbose_name=b'\xd0\x9a\xd1\x83\xd1\x80\xd1\x81', to='information.CourseNumber')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0435\u0434\u043c\u0435\u0442',
                'verbose_name_plural': '\u041f\u0440\u0435\u0434\u043c\u0435\u0442\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0')),
                ('document', models.FileField(upload_to=b'data/theory/', verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb')),
                ('lecture', models.OneToOneField(verbose_name=b'\xd0\x9b\xd0\xb5\xd0\xba\xd1\x86\xd1\x96\xd1\x8f', to='information.Lecture')),
            ],
            options={
                'verbose_name': '\u0422\u0435\u043e\u0440\u0456\u044f',
                'verbose_name_plural': '\u0422\u0435\u043e\u0440\u0456\u0457',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0')),
                ('document', models.FileField(upload_to=b'data/video/', verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb')),
                ('lecture', models.OneToOneField(verbose_name=b'\xd0\x9b\xd0\xb5\xd0\xba\xd1\x86\xd1\x96\xd1\x8f', to='information.Lecture')),
            ],
            options={
                'verbose_name': '\u0412\u0456\u0434\u0435\u043e\u0444\u0430\u0439\u043b',
                'verbose_name_plural': '\u0412\u0456\u0434\u0435\u043e\u0444\u0430\u0439\u043b\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='practicalwork',
            name='subject',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbc\xd0\xb5\xd1\x82', to='information.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lecture',
            name='subject',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbc\xd0\xb5\xd1\x82', to='information.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='checktest',
            name='subject',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbc\xd0\xb5\xd1\x82', to='information.Subject'),
            preserve_default=True,
        ),
    ]
