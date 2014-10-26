from django.db import models
from django.contrib.auth.models import User


class RegistrationProfile(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User)
    token = models.CharField(max_length=32)
    encoded = models.CharField(max_length=512)

    def __str__(self):
        return '{username}: {email}'.format(
            username=self.user.username,
            email=self.user.email
        )

    def __unicode__(self):
        return u'{0}'.format(self.__str__())


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(blank=True, null=True)
    friends = models.ManyToManyField('UserProfile', through='Friendship')

    def __str__(self):
        return '{username}: {email}'.format(
            username=self.user.username,
            email=self.user.email
        )

    def __unicode__(self):
        return u'{0}'.format(self.__str__())


class Friendrip(models.Model):
    friendee = models.ForeignKey(UserProfile)
    friend = models.ForeignKey(UserProfile)
    since = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    until = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{user} friend with {fiend}'.format(
            user=friendee.user.email,
            friend=friend.user.email
        )

    def __unicode__(self):
        return u'{0}'.format(self.__str__())
