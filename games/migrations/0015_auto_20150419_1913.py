# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0014_auto_20150419_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(related_name=b'games', null=True, to=b'userprofile.PlayerProfile', blank=True),
        ),
        migrations.AlterField(
            model_name='gameplayerdetail',
            name='player',
            field=models.ForeignKey(to='userprofile.PlayerProfile'),
        ),
        migrations.AlterField(
            model_name='phrase',
            name='player',
            field=models.ForeignKey(to='userprofile.PlayerProfile'),
        ),
    ]
