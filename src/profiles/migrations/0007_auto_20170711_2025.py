# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-11 18:25
from __future__ import unicode_literals

from django.db import migrations

def populate_team_responsible_public_credit_names(apps, schema_editor):
    Profile = apps.get_model("profiles", "Profile")
    TeamMember = apps.get_model("teams", "TeamMember")
    Team = apps.get_model("teams", "TeamMember")

    for team in Team.objects.all():
        if TeamMember.objects.filter(team=team, responsible=True).exists():
            responsibles = User.objects.filter(teammember__team=team, teammember__responsible=True)
        else:
            responsibles = team.area.responsible.all()
        for resp in responsibles:
            if not resp.profile.public_credit_name:
                profile = resp.profile
                profile.public_credit_name = resp.profile.name
                profile.save()


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20170711_1757'),
        ('teams', '0014_remove_teammember_deleted'),
    ]

    operations = [
        migrations.RunPython(populate_team_responsible_public_credit_names),
    ]
