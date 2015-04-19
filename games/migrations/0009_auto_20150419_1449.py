# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_player_is_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('game', models.ForeignKey(to='games.Game')),
                ('player', models.ForeignKey(to='games.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='player',
            name='game',
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(to='games.Player', blank=True),
            preserve_default=True,
        ),
    ]
