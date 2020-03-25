from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.


class Plant(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=1200, default='')
    cura = models.CharField(max_length=100, default='')

    def __str__(self):
        return "Planta: {0} y CURA: {1}".format(self.name, self.cura)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class Malestares(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=1200, default='', help_text="Adiciona observaciones/informacion")

    def __str__(self):
        return "Malestar: {0} y Observacion: {1}".format(self.name, self.description)

class Post(models.Model):
    post = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)