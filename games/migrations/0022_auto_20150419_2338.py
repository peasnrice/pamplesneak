# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0021_auto_20150419_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='host',
            field=models.ForeignKey(blank=True, to='games.Player', null=True),
        ),
    ]
