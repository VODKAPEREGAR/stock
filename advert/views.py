from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

Advert = Advert

# Create your views here.
def advert_view(request):
    return render(request, 'advert/advert.html')

def category_view(request):
    return render(request, 'advert/category.html')

def subcategory_view(request):
    return render(request, 'advert/subcategory.html')

@login_required(login_url=reverse_lazy('account:login'))
def add_view(request):
    if request.method == 'POST':
        form = AdvertAdd(request.POST)
        if form.is_valid():
            advert = Advert(
                title=form.cleaned_data['title'],
                category=form.cleaned_data['category'],
                subcategory=form.cleaned_data['subcategory'],
                city=form.cleaned_data['city'],
                price=form.cleaned_data['price'],
                description=form.cleaned_data['description'],
            )
            advert.save()
            return redirect(reverse('account:settings'))
    else:
        form = AdvertAdd()
    return render(request, 'advert/add.html', {'form': form})