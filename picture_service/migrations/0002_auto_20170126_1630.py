# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
