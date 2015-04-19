# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_auto_20150419_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerprofile',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 19, 19, 7, 51, 795151), editable=False),
            preserve_default=False,
        ),
    ]
