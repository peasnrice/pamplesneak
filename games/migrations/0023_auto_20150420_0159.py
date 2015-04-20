# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0022_auto_20150419_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameplayerdetail',
            name='game',
            field=models.ForeignKey(related_name=b'gpdgame', to='games.Game'),
        ),
        migrations.AlterField(
            model_name='gameplayerdetail',
            name='player',
            field=models.ForeignKey(related_name=b'gpdplayer', to='games.Player'),
        ),
    ]
