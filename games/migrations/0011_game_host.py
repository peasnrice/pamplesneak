# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_auto_20150419_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='host',
            field=models.ForeignKey(default=0, to='games.Player'),
            preserve_default=False,
        ),
    ]
