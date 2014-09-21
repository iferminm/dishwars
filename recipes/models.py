from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=128)
    

class Step(models.Model):
    action = models.TextField()
    recipe = models.ForeignKey(Recipe)


class Recipe(models.Model):
    ingredients = models.ManyToManyField(Ingredient, through=RecipeIngredient)


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=32)
    
