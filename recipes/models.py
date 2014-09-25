from django.db import models
from django.contrib.auth.models import User

from dishes.models import Dish

from .constants import TIME_UNIT_CHOICES, INGREDIENT_UNIT_CHOICES


class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'{name}'.format(name=self.name)


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

    def __unicode__(self):
        return u'{dish} by {author}'.format(dish=self.dish.name, 
                author=self.author.get_full_name())


class Step(models.Model):
    photo = models.ImageField(blank=True, null=True)
    directions = models.TextField()
    time = models.PositiveIntegerField()
    unit = models.CharField(max_length=20, choices=TIME_UNIT_CHOICES)
    order = models.PositiveIntegerField()
    recipe = models.ForeignKey(Recipe)

    def __unicode__(self):
        return u'{number} {recipe}'.format(number=self.order, recipe=self.recipe)


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)
    quantity = models.CharField(max_length=5)
    unit = models.CharField(max_length=20, choices=INGREDIENT_UNIT_CHOICES)

    def __unicode__(self):
        return u'{ingredient} on {recipe}'.format(ingredient=self.ingredient, recipe=self.recipe)


class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews')
    recipe = models.ForeignKey(Recipe, related_name='reviews')
    points = models.SmallIntegerField()
    comment = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'{user} on {recipe}'.format(user=self.user.get_full_name(), recipe=self.recipe)
