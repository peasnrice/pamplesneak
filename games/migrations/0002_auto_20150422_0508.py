# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_squashed_0024_remove_game_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phrase',
            name='game',
            field=models.ForeignKey(to='games.Game'),
        ),
        migrations.AlterField(
            model_name='player',
            name='created_on',
            field=models.DateTimeField(editable=False),
        ),
    ]
