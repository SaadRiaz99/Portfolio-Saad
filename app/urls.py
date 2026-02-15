
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),          
    path('home.html', views.Home, name="home"),          
    path('navbar.html', views.navbar, name="navbar"),
    path('about.html', views.about, name="about"),
    path('skill.html', views.skill, name="skill"),
    path('contact.html', views.contact, name="contact"),
]
