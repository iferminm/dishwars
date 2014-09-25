from django.db import models


class Cuisine(models.Model):
    name = models.CharField(max_length=160)

    def __unicode__(self):
        return u'%s' % self.name


class MealType(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return u'%s' % self.name


class Dish(models.Model):
    name = models.CharField(max_length=250)
    cuisine = models.ForeignKey(Cuisine, related_name='dishes')
    usually_taken = models.ManyToManyField(MealType, related_name='dishes')

    def __unicode__(self):
        return u'%s' % self.name

