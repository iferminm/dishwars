from django.db import models

# Create your models here.
class Cuisine(models.Model):
    name = models.CharField(max_length=128)


class Restaurant(models.Model):
    name = models.CharField(max_length=512)
    about = models.TextField()
    address = models.TextField()
    refferences = models.TextField(required=False)
    cuisines = models.ManyToManyfield(Cuisine)

