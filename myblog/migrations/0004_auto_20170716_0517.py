# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20170716_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybloguser',
            name='profilepic',
            field=models.FileField(upload_to=b''),
        ),
    ]
