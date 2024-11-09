from django.shortcuts import render, redirect
from .models import Profile


# Create your views here.


def Home(request):
    prof = Profile.objects.filter(name__icontains='a')
    print(prof)
    return render(request, 'home.html', locals())


def new_text():
    return 0 

def new_text_2():
    pass

def for_mursalin():
    pass