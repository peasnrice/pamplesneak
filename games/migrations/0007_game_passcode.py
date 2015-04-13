# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_auto_20150412_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='passcode',
            field=models.CharField(max_length=16, null=True),
            preserve_default=True,
        ),
    ]
