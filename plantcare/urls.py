from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_plant_care, name='plantcare'),
    path('water/', views.water_care, name='water_care'),
    path('sun/', views.sun_care, name='sun_care'),
    path('earth/', views.earth_care, name='earth_care'),
    path('air/', views.air_care, name='air_care'),
]