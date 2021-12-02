from django.contrib.auth import (
    authenticate,
    get_user_model,
    login as login_user,
    logout as logout_user
)
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import *
from .models import *


User = get_user_model()


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('account:settings'))
    if request.method == 'POST':
        form = ProfileRegister(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                city=form.cleaned_data['city'],
                gender=form.cleaned_data['gender'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(reverse('account:login'))
    else:
        form = ProfileRegister()
    return render(request, 'account/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('account:settings'))
    if request.method == 'POST':
        form = ProfileLogin(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login_user(request, user)
                return redirect(reverse('index'))
    else:
        form = ProfileLogin()
    return render(request, 'account/login.html', {'form': form})


def logout(request):
    logout_user(request)
    return redirect(reverse('account:login'))


def settings(request):
    return render(request, 'account/settings.html')
