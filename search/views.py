from django.shortcuts import render, redirect
from utils import get_client

# database connections
db_client = None
db_handle = None
users_collection = None
rides_collection  = None

def initialize_database():
    global db_client, db_handle, users_collection, rides_collection
    db_client = get_client()
    db_handle = db_client.main
    users_collection = db_handle.users
    rides_collection  = db_handle.rides

def search_index(request):
    initialize_database()

    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to create a ride."
        return redirect("index")

    all_rides = list(rides_collection.find())
    processed = []

    for ride in all_rides:
        ride["id"] = ride.pop("_id")
        processed.append(ride)
    return render(request, "search/search.html", {"username": request.session["username"], "rides": processed})
