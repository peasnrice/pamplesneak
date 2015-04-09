# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20150409_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='created_on',
            field=models.DateTimeField(default=datetime.date(2015, 4, 9), editable=False),
            preserve_default=False,
        ),
    ]
