from django.db import models
from django.contrib.auth.models import User

from dishes.models import Dish

from .constants import TIME_UNIT_CHOICES, INGREDIENT_UNIT_CHOICES


class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Recipe(models.Model):
    author = models.ForeignKey(User)
    dish = models.ForeignKey(Dish, related_name='recipes')
    ingredients = models.ManyToManyField(
            Ingredient,
            related_name='recipes',
            through='RecipeIngredient'
    )
    challenge_rate = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(default=0)


class Step(models.Model):
    photo = models.ImageField(blank=True, null=True)
    directions = models.TextField()
    time = models.PositiveIntegerField()
    unit = models.CharField(max_length=20, choices=TIME_UNIT_CHOICES)
    recipe = models.ForeignKey(Recipe)


class IngredientRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)
    quantity = models.CharField(max_length=5)
    unit = models.CharField(max_length=20, choices=INGREDIENT_UNIT_CHOICES)


class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews')
    recipe = models.ForeignKey(Recipe, related_name='reviews')
    points = models.SmallIntegerField()
    comment = models.TextField(null=True, blank=True)

