from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    
    path('stars/', views.stars_index, name='index'),
    path('stars/create/', views.StarCreate.as_view(), name='stars_create'),
    path('stars/<int:star_id>/', views.stars_detail, name='detail'),
    path('stars/<int:pk>/update/', views.StarUpdate.as_view(), name='stars_update'),
    path('stars/<int:pk>/delete/', views.StarDelete.as_view(), name='stars_delete'),

    path('stars/<int:star_id>/add_star_photo/', views.add_star_photo, name='add_star_photo'),
    path('stars/<int:star_id>/add_planet/<int:planet_id>/', views.add_planet, name='add_planet'),

    path('stars/<int:pk>/assoc_star/', views.StarMissionUpdate.as_view(), name='assoc_star'),
    path('stars/<int:star_id>/dissoc_star/<int:mission_id>/', views.dissoc_star, name='dissoc_star'),

 
    path('planets/', views.planets_index, name='planets_index'),
    path('planets/create/', views.PlanetCreate.as_view(), name='planets_create'),
    path('planets/<int:planet_id>/', views.planets_detail, name='planets_detail'),
    path('planets/<int:pk>/update/', views.PlanetUpdate.as_view(), name='planets_update'),
    path('planets/<int:pk>/delete/', views.PlanetDelete.as_view(), name='planets_delete'),

    path('planets/<int:planet_id>/add_planet_photo/', views.add_planet_photo, name='add_planet_photo'),
    path('planets/<int:planet_id>/add_satellite/<int:satellite_id>/', views.add_satellite, name='add_satellite'),
	
    path('planets/<int:pk>/assoc_planet/', views.PlanetMissionUpdate.as_view(), name='assoc_planet'),
    path('planet/<int:planet_id>/dissoc_planet/<int:mission_id>/', views.dissoc_planet, name='dissoc_planet'),

	   path('satellites/', views.satellites_index, name='satellites_index'),
    path('satellites/create/', views.SatelliteCreate.as_view(), name='satellites_create'),
    path('satellites/<int:satellite_id>/', views.satellites_detail, name='satellites_detail'),
    path('satellites/<int:pk>/update/', views.SatelliteUpdate.as_view(), name='satellites_update'),
    path('satellites/<int:pk>/delete/', views.SatelliteDelete.as_view(), name='satellites_delete'),
	   
	   path('satellites/<int:satellite_id>/add_satellite_photo/', views.add_satellite_photo, name='add_satellite_photo'),
				
    path('satellites/<int:pk>/assoc_satellite/', views.SatelliteMissionUpdate.as_view(), name='assoc_satellite'),
    path('satellites/<int:satellite_id>/dissoc_satellite/<int:mission_id>/', views.dissoc_satellite, name='dissoc_satellite'),

   	path('missions/', views.missions_index, name='missions_index'),
    path('missions/create/', views.MissionCreate.as_view(), name='missions_create'),
    path('missions/<int:mission_id>/', views.missions_detail, name='missions_detail'),
    path('missions/<int:pk>/update/', views.MissionUpdate.as_view(), name='missions_update'),
    path('missions/<int:pk>/delete/', views.MissionDelete.as_view(), name='missions_delete'),
]