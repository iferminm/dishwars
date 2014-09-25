from django.db import models


class Cuisine(models.Model):
    name = models.CharField(max_length=160)


class MealType(models.Model):
    name = models.CharField(max_length=150)


class Dish(models.Model):
    name = models.CharField(max_length=250)
    cuisine = models.ForeignKey(Cuisine, related_name='dishes')
    usually_taken = models.ManyToManyField(MealType, related_name='dishes')
