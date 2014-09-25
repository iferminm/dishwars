from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=512)
    about = models.TextField()
    address = models.TextField()
    refferences = models.TextField(required=False)
    cuisines = models.ManyToManyfield(Cuisine)

