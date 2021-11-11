from django.contrib import admin
# import your models here
from .models import StarPhoto, PlanetPhoto, SatellitePhoto, Star, Planet, Satellite, Mission

# Register your models here
admin.site.register(StarPhoto)
admin.site.register(PlanetPhoto)
admin.site.register(SatellitePhoto)
admin.site.register(Star)
admin.site.register(Planet)
admin.site.register(Satellite)
admin.site.register(Mission)