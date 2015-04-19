# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_auto_20150419_1920'),
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
    ]
