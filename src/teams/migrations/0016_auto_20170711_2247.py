# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-11 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0015_team_mailing_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='camp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='camps.Camp'),
        ),
    ]