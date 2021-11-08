from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import os
import boto3
from .models import Star, Planet, Satellite

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
    star = Star.objects.get(id=star_id)
    return render(request, 'stars/detail.html', {
        'star': star,
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







def planets_index(request):
    planets = Planet.objects.all()
    return render(request, 'planets/index.html', {'planets': planets})

def planets_detail(request, planet_id):
    planet = Planet.objects.get(id=planet_id)
    return render(request, 'planets/detail.html', {
        'planet': planet,
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
