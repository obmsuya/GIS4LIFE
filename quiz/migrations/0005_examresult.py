# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-21 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_quiz_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='', max_length=250)),
                ('username', models.CharField(default='', max_length=250)),
                ('course', models.CharField(default='', max_length=250)),
                ('phone', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Exam Result',
            },
        ),
    ]
