# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(max_length=50, upload_to='product', verbose_name='图片'),
        ),
    ]
