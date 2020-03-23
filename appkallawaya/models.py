from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.


class Plant(models.Model):
    name = models.CharField(max_length=100, default='00')
    description = models.CharField(max_length=1200, default='')

    def __str__(self):
        return "{0} ==> {1}".format(self.name, self.description)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
