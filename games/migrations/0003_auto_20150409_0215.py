# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='phrase',
            name='game',
            field=models.ForeignKey(default=1, to='games.Game'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phrase',
            name='player',
            field=models.ForeignKey(default=1, to='games.Player'),
            preserve_default=False,
        ),
    ]
