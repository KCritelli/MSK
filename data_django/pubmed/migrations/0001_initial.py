# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abstracts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=250)),
                ('journal', models.CharField(max_length=250)),
                ('abstract', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.CharField(max_length=50)),
                ('gene', models.CharField(max_length=100)),
                ('variation', models.CharField(max_length=250)),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
    ]
