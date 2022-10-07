from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests

def search_index(request):
    return render(request, 'search/search.html', {"username": request.session['username']})
    