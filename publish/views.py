from http.client import HTTPResponse
from django.shortcuts import render,redirect
from numpy import True_, dtype
import requests
import json
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from publish.forms import RideForm
from utils import get_client
# from django.http import HttpResponse

# Create your views here.
client = get_client()
db = client.SEProject
ridesDB  = db.rides
routesDB  = db.routes

def publish_index(request):
    if not request.session.has_key('username'):
        request.session['alert'] = "Please login to create a ride."
        return redirect('index')
    return render(request, 'publish/publish.html', {"username": request.session['username'], "alert":True})

def display_ride(request, ride_id):
    ride = ridesDB.find_one({'_id': ride_id})
    routes = get_routes(ride)
    
    context = {
            "username": request.session['username'],
            "ride": ride,
            "routes": routes
        }
    return render(request, 'publish/route.html', context)

def get_routes(ride):
    routes = []
    if 'routes' not in ride:
        return None
    route_ids = ride['routes']
    for route_id in route_ids:
        route = routesDB.find_one({'_id': route_id})
        route['id'] = route.pop('_id')
        routes.append(route)
    return routes

def create_ride(request):
    if request.method == 'POST':
        ride = {
            "_id": 
                request.POST.get('name')+"_"+request.POST.get('destination')
                +"_"+request.POST.get("date")+"_"+
                request.POST.get("hour")+"_"+
                request.POST.get("minute")+"_"+
                request.POST.get("ampm")
            ,
                "name": request.POST.get('name'),
                "destination": request.POST.get('destination'),
                "date": request.POST.get("date"),
                "hour": request.POST.get("hour"),
                "minute":  request.POST.get("minute"),
                "ampm": request.POST.get("ampm"),
                "details": request.POST.get("details")
            }
        request.session['ride'] = ride
        if ridesDB.find_one({'_id': ride['_id']})== None:
            ridesDB.insert_one(ride)
        return redirect(display_ride, ride_id=request.session['ride']['_id'] )

    return render(request, 'publish/publish.html', {"username": request.session['username']})

def add_route(request):
    if request.method == 'POST':
        
        ride = request.POST.get('ride')
        ride = ride.replace("\'", "\"")
        ride = json.loads(ride)
        ride_id = ride['_id']
        ride = ridesDB.find_one({'_id': ride['_id']})
        route = {
                "_id": str(ride_id)
                +"_"+request.POST.get('type')
                +"_"+request.POST.get('spoint')
                +"_"+request.POST.get("hour")
                +"_"+request.POST.get("minute")
                +"_"+request.POST.get("duration")
                +"_"+request.POST.get("details")
                +"_"+request.POST.get("ampm"),

                "type": request.POST.get('type'),
                "spoint": request.POST.get('spoint'),
                "hour": request.POST.get("hour"),
                "minute":  request.POST.get("minute"),
                "duration": request.POST.get("duration"),
                "details": request.POST.get("details"),
                "ampm": request.POST.get("ampm"),
                "users": [request.session['username']]
            }
        request.session["route"] = route
        request.session["ride"] = ride
        #check if route is unique
        if routesDB.find_one({'_id': route["_id"]})== None:
            routesDB.insert_one(route)
            if 'routes' not in ride:
                ridesDB.update_one({"_id": ride_id}, {"$set": {"routes": [route['_id']]}})
            else:
                ride['routes'].append(route['_id'])
                ridesDB.update_one({"_id": ride_id}, {"$set": {"routes": ride['routes']}})
        return redirect(display_ride, ride_id=request.session['ride']['_id'] )

    return render(request, 'publish/publish.html', {"username": request.session['username']})




