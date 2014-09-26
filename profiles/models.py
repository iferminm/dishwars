from django.db import models
from django.contrib.auth.models import User


class RegistrationProfile(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User)
    token = models.CharField(max_length=32)
    encoded = models.CharField(max_length=512)


class UserProfile(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User)
    avatar = models.ImageField(blank=True, null=True)

