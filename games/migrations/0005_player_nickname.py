# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_player_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='nickname',
            field=models.CharField(default='noob', max_length=64),
            preserve_default=False,
        ),
    ]
