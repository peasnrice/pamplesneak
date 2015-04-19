# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20150409_0153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nickname',
            name='userprofile',
        ),
        migrations.DeleteModel(
            name='Nickname',
        ),
    ]
