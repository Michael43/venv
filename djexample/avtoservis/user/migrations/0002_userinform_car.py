# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_auto_20160410_0516'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinform',
            name='car',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, to='car.CarModel'),
            preserve_default=False,
        ),
    ]