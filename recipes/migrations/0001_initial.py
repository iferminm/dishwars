# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('photo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('challenge_rate', models.PositiveIntegerField()),
                ('rating', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('dish', models.ForeignKey(related_name=b'recipes', to='dishes.Dish')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.CharField(max_length=5)),
                ('unit', models.CharField(max_length=20, choices=[(b'pinch', b'Pinch'), (b'teaspoon', b'Teaspoon'), (b'tablespoon', b'Tablespoon'), (b'cup', b'Cups'), (b'glass', b'Glass'), (b'litre', b'Litres'), (b'gram', b'Grams'), (b'kilo', b'Kilos')])),
                ('ingredient', models.ForeignKey(to='recipes.Ingredient')),
                ('recipe', models.ForeignKey(to='recipes.Recipe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.SmallIntegerField()),
                ('comment', models.TextField(null=True, blank=True)),
                ('recipe', models.ForeignKey(related_name=b'reviews', to='recipes.Recipe')),
                ('user', models.ForeignKey(related_name=b'reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('directions', models.TextField()),
                ('time', models.PositiveIntegerField()),
                ('unit', models.CharField(max_length=20, choices=[(b'seconds', b'Seconds'), (b'minutes', b'Minutes'), (b'hours', b'Hours'), (b'days', b'Days'), (b'weeks', b'Weeks')])),
                ('order', models.PositiveIntegerField()),
                ('recipe', models.ForeignKey(to='recipes.Recipe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name=b'recipes', through='recipes.RecipeIngredient', to='recipes.Ingredient'),
            preserve_default=True,
        ),
    ]
