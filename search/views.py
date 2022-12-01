from django.shortcuts import render, redirect
from utils import get_client

client = None
db = None
userDB = None
ridesDB  = None
routesDB  = None

def intializeDB():
    global client, db, userDB, ridesDB, routesDB
    client = get_client()
    db = client.SEProject
    userDB = db.userData
    ridesDB  = db.rides
    routesDB  = db.routes

def search_index(request):
    intializeDB()
    if not request.session.has_key('username'):
        request.session['alert'] = "Please login to create a ride."
        return redirect('index')
    all_rides = list(ridesDB.find())
    processed = list()
    for ride in all_rides:
        ride['id'] = ride.pop('_id')
        processed.append(ride)
    return render(request, 'search/search.html', {"username": request.session['username'], "rides":processed})
    