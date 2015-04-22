# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0023_auto_20150420_0159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='players',
        ),
    ]
