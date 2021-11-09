from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PlanetForm, StarForm
import uuid
import os
import boto3
from .models import Star, Planet, Satellite, Mission, StarPhoto, PlanetPhoto, SatellitePhoto

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def stars_index(request):
    stars = Star.objects.all()
    return render(request, 'stars/index.html', {'stars': stars})


def stars_detail(request, star_id):
    star_form = StarForm()
    star = Star.objects.get(id=star_id)
    planets_star_doesnt_have = Planet.objects.exclude(
        id__in=star.planet_set.all().values_list('id'))

    return render(request, 'stars/detail.html', {
        'star': star,
								'planets': planets_star_doesnt_have,
								'star_form' : star_form
    })


class StarCreate(LoginRequiredMixin, CreateView):
    model = Star
    fields = ['name', 'star_type', 'mass',
              'diameter', 'distance', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StarUpdate(LoginRequiredMixin, UpdateView):
    model = Star
    fields = ['star_type', 'mass', 'diameter', 'description']


class StarDelete(LoginRequiredMixin, DeleteView):
    model = Star
    success_url = '/stars/'


def add_planet(request, star_id, planet_id):
    planet = Planet.objects.get(id=planet_id)
    planet.star_id = star_id
    planet.save()
    return redirect('detail', star_id=star_id,)


def planets_index(request):
    planets = Planet.objects.all()
    return render(request, 'planets/index.html', {'planets': planets})


def planets_detail(request, planet_id):
    planet_form = PlanetForm()
    planet = Planet.objects.get(id=planet_id)
    return render(request, 'planets/detail.html', {
        'planet': planet,
        'planet_form': planet_form,
    })


class PlanetCreate(LoginRequiredMixin, CreateView):
    model = Planet
    fields = ['name', 'planet_type', 'mass',
              'diameter', 'distance', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlanetUpdate(LoginRequiredMixin, UpdateView):
    model = Planet
    fields = ['planet_type', 'mass', 'diameter', 'description']


class PlanetDelete(LoginRequiredMixin, DeleteView):
    model = Planet
    success_url = '/planets/'

def add_satellite(request, planet_id, satellite_id):
    satellite = Satellite.objects.get(id=satellite_id)
    satellite.planet_id = planet_id
    satellite.save()
    return redirect('detail', planet_id=planet_id,)

def satellites_index(request):
    satellites = Satellite.objects.all()
    return render(request, 'satellites/index.html', {'satellites': satellites})


def satellites_detail(request, satellite_id):
    satellite = Satellite.objects.get(id=satellite_id)
    return render(request, 'satellites/detail.html', {
        'satellite': satellite
    })


class SatelliteCreate(LoginRequiredMixin, CreateView):
    model = Satellite

    fields = ['name', 'satellite_type', 'mass',
              'diameter', 'distance', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SatelliteUpdate(LoginRequiredMixin, UpdateView):
    model = Satellite

    fields = ['satellite_type', 'mass', 'diameter', 'description']


class SatelliteDelete(LoginRequiredMixin, DeleteView):
    model = Satellite

    success_url = '/satellites/'


def missions_index(request):
    missions = Mission.objects.all()
    return render(request, 'missions/index.html', {'missions': missions})


def missions_detail(request, mission_id):
    mission = Mission.objects.get(id=mission_id)
    return render(request, 'missions/detail.html', {
        'mission': mission
    })


class MissionCreate(LoginRequiredMixin, CreateView):
    model = Mission

    fields = ['name', 'mission_type', 'launched',
              'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MissionUpdate(LoginRequiredMixin, UpdateView):
    model = Mission
    fields = ['name', 'mission_type', 'launched',
              'description']


class MissionDelete(LoginRequiredMixin, DeleteView):
    model = Mission

    success_url = '/missions/'


def assoc_mission(request, star_id, mission_id):
    Star.objects.get(id=star_id).star.add(mission_id)
    return redirect('detail', star_id=star_id)


def dissoc_mission(request, star_id, mission_id):
    Star.objects.get(id=star_id).star.remove(mission_id)
    return redirect('detail', star_id=star_id)

def add_star_photo(request, star_id):
    # the form's input will have a name of photo-file
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url sting
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            StarPhoto.objects.create(url=url, star_id=star_id)
        except Exception as e:
            print('An error occured uploading file to S3', e)
    return redirect('detail', star_id=star_id)

def add_planet_photo(request, planet_id):
    # the form's input will have a name of photo-file
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url sting
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            PlanetPhoto.objects.create(url=url, planet_id=planet_id)
        except Exception as e:
            print('An error occured uploading file to S3', e)
    return redirect('planets_detail', planet_id=planet_id)

def add_satellite_photo(request, satellite_id):
    # the form's input will have a name of photo-file
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url sting
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            SatellitePhoto.objects.create(url=url, satellite_id=satellite_id)
        except Exception as e:
            print('An error occured uploading file to S3', e)
    return redirect('satellites_detail', satellite_id=satellite_id)