# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_userprofile_nicknames'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='nicknames',
        ),
    ]
