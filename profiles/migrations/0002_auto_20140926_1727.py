# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationprofile',
            old_name='created_at',
            new_name='created_on',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 26, 17, 26, 38, 87035), auto_now_add=True),
            preserve_default=False,
        ),
    ]
