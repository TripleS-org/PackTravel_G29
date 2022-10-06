from http.client import HTTPResponse
from django.shortcuts import render,redirect
import requests
import json
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from publish.forms import CreateNewRide
from user.views import userDB, index
from utils import get_client
# from django.http import HttpResponse

# Create your views here.
# from django.http import HttpResponse

def publish_index(request):
    return render(request, 'publish/publish.html')

def route(request):
    return render(request, 'publish/route.html')

def createNewRide(request):
    if request.method == "POST":
        form = CreateNewRide(request.POST)
        if form.is_valid():
            userObj = {
                "destination": form.cleaned_data["destination"],
                "rideDate": form.cleaned_data["rideDate"]
            }
            userDB.insert_one(userObj)
            request.session['destination'] = userObj["destination"]
            request.session['rideDate'] = userObj["rideDate"]
            return redirect(index, username=request.session["username"])
        else:
            print(form.errors.as_data())
    else:
        if request.session.has_key('username'):
            return index(request,request.session['username'])
        form = CreateNewRide()
    return render(request, 'user/register.html', {"form": form})
