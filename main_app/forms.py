from django.forms import ModelForm
from .models import Planet, Star

class PlanetForm(ModelForm):
    class Meta:
        model = Planet 
        fields = ['name', 'planet_type']


class StarForm(ModelForm):
    class Meta:
        model = Star
        fields = ['name', 'star_type']