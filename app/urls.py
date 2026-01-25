
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home.html', views.Home, name="home"),          
    path('navbar.html', views.navbar, name="navbar"),
    path('about.html', views.about, name="about"),
    path('skill.html', views.skill, name="skill"),
]
