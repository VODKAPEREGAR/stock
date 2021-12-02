from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('advert/', include('advert.urls')),
    path('', include('main.urls')),
]