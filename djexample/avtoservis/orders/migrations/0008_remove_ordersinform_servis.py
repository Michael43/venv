# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 09:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20160421_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordersinform',
            name='servis',
        ),
    ]
