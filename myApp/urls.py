from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('', views.index, name='myApp'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact')
]