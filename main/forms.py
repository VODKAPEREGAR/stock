from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class SendHelp(forms.ModelForm):
    class Meta(UserCreationForm):
        model = Help
        fields = [
            ('title'),
            ('description'),
            ('emanil'),
        ]