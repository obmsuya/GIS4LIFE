# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-01 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_delete_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestGrades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('firstname', models.CharField(blank=True, max_length=60, null=True)),
                ('grade', models.CharField(blank=True, max_length=10, null=True)),
                ('quiz_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='UserGrades',
            new_name='ExamGrades',
        ),
    ]
