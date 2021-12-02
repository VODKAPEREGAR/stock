from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout, name='logout'),
]


