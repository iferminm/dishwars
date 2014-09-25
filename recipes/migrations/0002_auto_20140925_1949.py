# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(max_length=20, choices=[(b'pinch', b'Pinch'), (b'teaspoon', b'Teaspoon'), (b'tablespoon', b'Tablespoon'), (b'cup', b'Cups'), (b'glass', b'Glass'), (b'litre', b'Litres'), (b'gram', b'Grams'), (b'kilo', b'Kilos'), (b'units', b'Units')]),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('user', 'recipe')]),
        ),
    ]
