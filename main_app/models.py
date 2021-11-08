from django.urls import reverse
from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


class Star(models.Model):
    name = models.CharField(max_length=50)
    star_type = models.CharField(max_length=50)
    mass = models.CharField(max_length=50)
    diameter = models.CharField(max_length=50)
    distance = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # missions = models.ManyToManyField(Missions) #ADD LATER ALONG W MODEL
  # users = models.ManyToManyField(Users) #ADD LATER TOO

    def __str__(self):
        return f'({self.id}) - {self.name}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'star_id': self.id})


class Planet(models.Model):
    name = models.CharField(max_length=50)
    planet_type = models.CharField(max_length=50)
    mass = models.CharField(max_length=50)
    diameter = models.CharField(max_length=50)
    distance = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # missions = models.ManyToManyField(Missions) #ADD LATER ALONG W MODEL
  # users = models.ManyToManyField(Users) #ADD LATER TOO

    def __str__(self):
        return f'({self.id}) - {self.name}'

    def get_absolute_url(self):
        return reverse('planets_detail', kwargs={'planet_id': self.id})


class Satellite(models.Model):
    name = models.CharField(max_length=50)
    satellite_type = models.CharField(max_length=50)
    mass = models.CharField(max_length=50)
    diameter = models.CharField(max_length=50)
    distance = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # missions = models.ManyToManyField(Missions) #ADD LATER ALONG W MODEL
  # users = models.ManyToManyField(Users) #ADD LATER TOO

    def __str__(self):
        return f'({self.id}) - {self.name}'

    def get_absolute_url(self):
        return reverse('satellites_detail', kwargs={'satellite_id': self.id})

