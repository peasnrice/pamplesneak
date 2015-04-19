# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_game_passcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_host',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
