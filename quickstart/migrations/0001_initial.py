# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('placas', models.CharField(max_length=30)),
            ],
        ),
    ]
