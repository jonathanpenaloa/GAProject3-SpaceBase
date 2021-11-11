from django.forms import ModelForm
from .models import Planet, Star, Satellite

class PlanetForm(ModelForm):
    class Meta:
        model = Planet 
        fields = ['name', 'planet_type']


class StarForm(ModelForm):
    class Meta:
        model = Star
        fields = ['name', 'star_type']
        
class StarMissionForm(ModelForm):
    class Meta:
        model = Star
        fields = ['missions']

class PlanetMissionForm(ModelForm):
    class Meta:
        model = Planet
        fields = ['missions']

class SatelliteMissionForm(ModelForm):
    class Meta:
        model = Satellite
        fields = ['missions']