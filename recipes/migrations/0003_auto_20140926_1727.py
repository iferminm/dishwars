# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20140925_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 26, 17, 26, 50, 490042), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 26, 17, 27, 14, 550085), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 26, 17, 27, 24, 226742), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 26, 17, 27, 31, 14060), auto_now=True),
            preserve_default=False,
        ),
    ]
