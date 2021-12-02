from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import *


class ProfileRegister(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta(UserCreationForm):
        model = Profile
        fields = [
            ('username'),
            ('email'),
            ('password'),
            ('first_name'),
            ('last_name'),
            ('city'),
            ('gender'),
        ]


class ProfileLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        if not user:
            raise ValidationError('Введенные данные не верны.')
        return self.cleaned_data
