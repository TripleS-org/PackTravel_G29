from django.shortcuts import render,redirect
import requests
import json
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Home page for PackTravel
def index(request):
    return render(request, 'home/home.html')


def home(request):
    return render(request, 'home/home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'user/register.html', context)
