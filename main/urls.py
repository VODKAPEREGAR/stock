from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('help', views.help, name='help'),
    path('rules', views.rules, name='rules'),
    path('ads', views.ads, name='ads'),
    path('', views.index, name='index'),
]
