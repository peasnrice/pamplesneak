# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'userprofile', '0001_initial'), (b'userprofile', '0002_userprofile_nicknames'), (b'userprofile', '0003_remove_userprofile_nicknames'), (b'userprofile', '0004_userprofile_nicknames'), (b'userprofile', '0005_remove_userprofile_nicknames'), (b'userprofile', '0006_auto_20150409_0153'), (b'userprofile', '0007_auto_20150419_1900'), (b'userprofile', '0008_auto_20150419_1905'), (b'userprofile', '0009_playerprofile_created_on'), (b'userprofile', '0010_auto_20150419_1920'), (b'userprofile', '0011_nickname'), (b'userprofile', '0012_auto_20150419_1934'), (b'userprofile', '0013_remove_userprofile_games_played_count'), (b'userprofile', '0014_userprofile_games_played_count'), (b'userprofile', '0001_squashed_0014_userprofile_games_played_count'), (b'userprofile', '0015_merge')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('games_played_count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('games_played_count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
