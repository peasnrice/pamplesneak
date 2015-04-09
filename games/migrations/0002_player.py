# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20150409_0153'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game', models.ForeignKey(to='games.Game')),
                ('userprofile', models.ForeignKey(to='userprofile.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
