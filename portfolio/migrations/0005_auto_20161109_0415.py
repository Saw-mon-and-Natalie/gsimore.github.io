# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20161103_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='small_image',
            field=models.ImageField(editable=False, upload_to=''),
        ),
        migrations.AlterField(
            model_name='piece',
            name='thumbnail_image',
            field=models.ImageField(editable=False, upload_to=''),
        ),
    ]
