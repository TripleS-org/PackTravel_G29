"""Django views for ride search functionality"""
from django.shortcuts import render, redirect
from utils import get_client
from request import views as requestsViews

# database connections
db_client = None
db_handle = None
users_collection = None
rides_collection  = None

def initialize_database():
    """This method initializes handles to the different database collections"""
    global db_client, db_handle, users_collection, rides_collection
    db_client = get_client()
    db_handle = db_client.main
    users_collection = db_handle.users
    rides_collection  = db_handle.rides

def search_index(request):
    """This method processes the request to render available rides on the search page"""
    initialize_database()

    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to view rides."
        return redirect("index")

    all_rides = list(rides_collection.find())
    processed = []

    for ride in all_rides:
        ride["id"] = ride.pop("_id")
        processed.append(ride)
    return render(request, "search/search.html", {"username": request.session["username"], "rides": processed})

def request_ride(request, ride_id):
    """This method processes the request from a user to be part of a ride"""
    initialize_database()

    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to request rides."
        return redirect("index")

    # get ride information from db
    ride = rides_collection.find_one({"_id": ride_id})

    # validation - check for edge cases
    if ride is not None:
        if ride["availability"] == 0:
            message = "Ride has reached max capacity."
        elif ride["owner"] == request.session["username"]:
            message = "Owner of the ride cannot request own rides."
        elif request.session["username"] in ride["confirmed_users"]:
            message = "You are already a confirmed member of this ride."
        else:
            # add/update request to ride
            rides_collection.update_one({"_id": ride_id}, {"$addToSet": {"requested_users": request.session["username"]}})
            message = "Request successful."
        print(message)

    return redirect(requestsViews.requested_rides)
