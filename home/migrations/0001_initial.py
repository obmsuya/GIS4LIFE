# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 10:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(default='', max_length=200)),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subtitle', models.CharField(default='Introduction to GIS', max_length=120)),
                ('description', models.TextField()),
                ('link', models.TextField(default='')),
                ('audience', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('price', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Category')),
            ],
            options={
                'verbose_name_plural': 'Item',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=120)),
                ('theory', models.CharField(default='', max_length=200)),
                ('practicle', models.CharField(default='', max_length=120)),
                ('exam', models.CharField(default='', max_length=120)),
                ('results', models.CharField(default='', max_length=120)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='', max_length=100)),
                ('username', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('region', models.CharField(default='', max_length=100)),
                ('Proffession', models.CharField(default='', max_length=100)),
                ('category', models.CharField(default='', max_length=100)),
                ('course', models.CharField(default='', max_length=100)),
                ('phone', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Students Request',
            },
        ),
    ]
