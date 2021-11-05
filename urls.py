from django.urls import pathfrom . import views

urlpatterns = [ 
				path('', views.home, name='home'),
]
