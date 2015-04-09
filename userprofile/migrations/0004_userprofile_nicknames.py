# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import custom.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_remove_userprofile_nicknames'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nicknames',
            field=custom.fields.SeparatedValuesField(default=''),
            preserve_default=False,
        ),
    ]
