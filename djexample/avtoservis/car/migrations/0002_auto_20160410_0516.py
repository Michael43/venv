# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 02:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='brand',
            new_name='model',
        ),
    ]