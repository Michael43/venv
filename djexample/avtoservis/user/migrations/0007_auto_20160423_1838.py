# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-23 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20160421_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinform',
            name='number',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinform',
            name='phone_number',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
    ]
