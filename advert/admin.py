from django.contrib import admin
from . import models



@admin.register(models.Advert)
class AdvertAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass