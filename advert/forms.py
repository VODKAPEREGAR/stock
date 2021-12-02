from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class AdvertAdd(forms.ModelForm):
    class Meta(UserCreationForm):
        model = Advert
        fields = [
            ('title'),
            ('category'),
            ('subcategory'),
            ('city'),
            ('price'),
            ('description'),
        ]