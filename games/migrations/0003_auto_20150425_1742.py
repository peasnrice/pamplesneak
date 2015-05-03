# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20150422_0508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phrase',
            old_name='player',
            new_name='recipient',
        ),
        migrations.RemoveField(
            model_name='phrase',
            name='game',
        ),
        migrations.AddField(
            model_name='phrase',
            name='gpd',
            field=models.ForeignKey(default=0, to='games.GamePlayerDetail'),
            preserve_default=False,
        ),
    ]
