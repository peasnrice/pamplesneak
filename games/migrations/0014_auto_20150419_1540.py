# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0013_auto_20150419_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePlayerDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('game', models.ForeignKey(to='games.Game')),
                ('player', models.ForeignKey(to='games.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='gameplayerdetails',
            name='game',
        ),
        migrations.RemoveField(
            model_name='gameplayerdetails',
            name='player',
        ),
        migrations.DeleteModel(
            name='GamePlayerDetails',
        ),
    ]
