from django.urls import reverse
from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class SpaceObject(models.Model):
		name = models.CharField(max_length=50)
		so_type = models.CharField(max_length=50)
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
				return reverse('detail', kwargs={'spaceobject_id': self.id})

class Photo(models.Model):
		url=models.CharField(max_length=200)
		ship=models.ForeignKey(SpaceObject, on_delete=models.CASCADE)

		def __str__(self):
				return f"Photo for spaceobject_id:{self.spaceobject_id}@{self.url}"