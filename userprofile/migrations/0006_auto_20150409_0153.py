# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_remove_userprofile_nicknames'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nickname',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname_text', models.CharField(max_length=32)),
                ('userprofile', models.ForeignKey(to='userprofile.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='games_played_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
