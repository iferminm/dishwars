from django.db import models


class Cuisine(models.Model):
    name = models.CharField(max_length=160)

    def __unicode__(self):
        return u'{cuisine}'.format(cuisine=self.name)


class MealType(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return u'{mealtype}'.format(mealtype=self.name)


class Dish(models.Model):
    name = models.CharField(max_length=250)
    cuisine = models.ForeignKey(Cuisine, related_name='dishes')
    usually_taken = models.ManyToManyField(MealType, related_name='dishes')

    class Meta:
        verbose_name_plural = 'Dishes'

    def __unicode__(self):
        return u'{dish_name}'.format(dish_name=self.name)

