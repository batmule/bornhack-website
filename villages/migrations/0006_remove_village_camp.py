# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('villages', '0005_auto_20160712_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='village',
            name='camp',
        ),
    ]