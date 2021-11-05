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
from .models import Star, Photo

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

@login_required
def stars_index(request):
				stars = Star.objects.all()
				return render(request, 'stars/index.html', {'stars': stars})

@login_required
def stars_detail(request, star_id):
  star = Star.objects.get(id=star_id)
  return render(request, 'stars/detail.html', {
    'star': star,
  })

class StarCreate(LoginRequiredMixin, CreateView):
		model = Star
		fields = ['name', 'star_type', 'mass', 'diameter', 'distance','description']
		def form_valid(self, form):
				form.instance.user=self.request.user
				return super().form_valid(form)

class StarUpdate(LoginRequiredMixin, UpdateView):
		model = Star
		fields = ['star_type', 'mass', 'diameter', 'description']

class StarDelete(LoginRequiredMixin, DeleteView):
		model = Star
		success_url = '/stars/'