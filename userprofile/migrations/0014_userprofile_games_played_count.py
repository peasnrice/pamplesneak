# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0013_remove_userprofile_games_played_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='games_played_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
