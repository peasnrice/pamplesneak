# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0012_auto_20150419_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='games_played_count',
        ),
    ]
