from http.client import HTTPResponse
from django.shortcuts import render,redirect
import requests
import json
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from utils import get_client
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse

def publish_index(request):
    return render(request, 'publish/publish.html')

def route(request):
    return render(request, 'publish/route.html')