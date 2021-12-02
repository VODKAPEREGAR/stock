from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse


from .forms import *
from .models import *
from advert.models import Advert
Help = Help


def index(request):
    advert = Advert.objects.all()
    context = {
        'advert': advert
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def help(request):
    if request.method == 'POST':
        form = SendHelp(request.POST)
        if form.is_valid():
            help = Help(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                emanil=form.cleaned_data['emanil'],
            )
            help.save()
            return redirect(reverse('index'))
    else:
        form = SendHelp()
    return render(request, 'main/help.html', {'form': form})
    
def rules(request):
    return render(request, 'main/rules.html')

def ads(request):
    return render(request, 'main/ads.html')