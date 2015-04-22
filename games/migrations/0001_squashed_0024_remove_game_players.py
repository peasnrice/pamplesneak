# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'games', '0001_initial'), (b'games', '0002_player'), (b'games', '0003_auto_20150409_0215'), (b'games', '0004_player_created_on'), (b'games', '0005_player_nickname'), (b'games', '0006_auto_20150412_2021'), (b'games', '0007_game_passcode'), (b'games', '0008_player_is_host'), (b'games', '0009_auto_20150419_1449'), (b'games', '0010_auto_20150419_1506'), (b'games', '0011_game_host'), (b'games', '0012_remove_player_is_host'), (b'games', '0013_auto_20150419_1538'), (b'games', '0014_auto_20150419_1540'), (b'games', '0015_auto_20150419_1913'), (b'games', '0016_auto_20150419_1915'), (b'games', '0017_auto_20150419_1941'), (b'games', '0018_auto_20150419_1945'), (b'games', '0019_auto_20150419_1953'), (b'games', '0020_auto_20150419_1955'), (b'games', '0021_auto_20150419_2015'), (b'games', '0022_auto_20150419_2338'), (b'games', '0023_auto_20150420_0159'), (b'games', '0024_remove_game_players')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),

    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('motto', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(editable=False)),
                ('passcode', models.CharField(max_length=16, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phrase_text', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(editable=False)),
                ('game', models.ForeignKey(default=1, to='games.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=datetime.date(2015, 4, 9), editable=False)),
                ('nickname', models.CharField(default=b'', max_length=64)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('game_count', models.IntegerField(default=0)),
                ('game_record', models.IntegerField(default=0)),
                ('hosted_count', models.IntegerField(default=0)),
                ('phrase_count', models.IntegerField(default=0)),
                ('phrase_record', models.IntegerField(default=0)),
                ('word_count', models.IntegerField(default=0)),
                ('word_record', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='phrase',
            name='player',
            field=models.ForeignKey(to='games.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(related_name=b'games', null=True, to=b'games.Player', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='host',
            field=models.ForeignKey(default=0, to='games.Player'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='GamePlayerDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('game', models.ForeignKey(related_name=b'gpdgame', to='games.Game')),
                ('player', models.ForeignKey(related_name=b'gpdplayer', to='games.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='game',
            name='players',
        ),
        migrations.AlterField(
            model_name='game',
            name='host',
            field=models.ForeignKey(blank=True, to='games.Player', null=True),
        ),
    ]
