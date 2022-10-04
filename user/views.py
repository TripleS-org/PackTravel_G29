from django.shortcuts import render
import requests
import json

# Home page for PackTravel
def index(request):
    return render(request, 'home/home.html')
