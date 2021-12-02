from django.contrib import admin
from . import models


@admin.register(models.Help)
class HelpAdmin(admin.ModelAdmin):
    pass