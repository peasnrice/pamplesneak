# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import custom.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nicknames',
            field=custom.fields.SeparatedValuesField(default=None),
            preserve_default=True,
        ),
    ]
