# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(default='ex@hotmail.com', max_length=200),
        ),
    ]
