# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0019_auto_20150419_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='nickname',
            field=models.CharField(default=b'', max_length=64),
        ),
    ]
