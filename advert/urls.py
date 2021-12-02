from django.urls import path
from . import views

urlpatterns = [
    path('', views.advert_view, name='advert'),
    path('add', views.add_view, name='add')
]