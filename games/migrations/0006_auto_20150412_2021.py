# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0005_player_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='userprofile',
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
