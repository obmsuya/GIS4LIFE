# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-05 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20190105_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='subtitle',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
