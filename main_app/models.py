from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

class Mission(models.Model):
    name = models.CharField(max_length=50)
    mission_type = models.CharField(max_length=50)
    launched = models.IntegerField( )
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('missions_detail', kwargs={'mission_id': self.id})


class Star(models.Model):
    name = models.CharField(max_length=50)
    star_type = models.CharField(max_length=50)
    mass = models.CharField(max_length=50)
    diameter = models.CharField(max_length=50)
    distance = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    missions = models.ManyToManyField(Mission, blank=True)

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
    missions = models.ManyToManyField(Mission, blank=True)
    star = models.ForeignKey(Star, on_delete=models.SET_NULL, blank=True, null=True)

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
    missions = models.ManyToManyField(Mission, blank=True) 
    planet = models.ForeignKey(Planet, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'({self.id}) - {self.name}'

    def get_absolute_url(self):
        return reverse('satellites_detail', kwargs={'satellite_id': self.id})

class StarPhoto(models.Model):
  url = models.CharField(max_length=200)
  star = models.ForeignKey(Star, on_delete=models.CASCADE)
  def __str__(self):
    return f"Photo for star_id: {self.star_id} @{self.url}"

class PlanetPhoto(models.Model):
  url = models.CharField(max_length=200)
  planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
  def __str__(self):
    return f"Photo for planet_id: {self.planet_id} @{self.url}"

class SatellitePhoto(models.Model):
  url = models.CharField(max_length=200)
  satellite = models.ForeignKey(Satellite, on_delete=models.CASCADE)
  def __str__(self):
    return f"Photo for satellite_id: {self.satellite_id} @{self.url}"
    