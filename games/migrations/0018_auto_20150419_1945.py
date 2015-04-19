# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0017_auto_20150419_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.OneToOneField(related_name=b'usersplayer', to=settings.AUTH_USER_MODEL),
        ),
    ]
