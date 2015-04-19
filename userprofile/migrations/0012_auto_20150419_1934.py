# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0011_nickname'),
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
