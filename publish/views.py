"""Django views for ride creation functionality"""
from django.shortcuts import render, redirect
from datetime import datetime
from cab_model.predict import predict_price
from utils import get_client
import uuid
import requests

# database connections
db_client = None
db_handle = None
users_collection = None
rides_collection = None

def initialize_database():
    """This method initialises the handles to various database collections"""
    global db_client, db_handle, users_collection, rides_collection
    db_client = get_client()
    db_handle = db_client.main
    users_collection = db_handle.users
    rides_collection = db_handle.rides

def publish_index(request):
    """This method processes the user request to see the publish - Create ride page"""
    initialize_database()
    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to create a ride."
        # return a meaningful message instead of simply redirecting.
        return redirect("index")
    return render(request, "publish/publish.html", {"username": request.session["username"], "alert": True})


def distance_and_cost(source, destination, date, hour, minute, ampm):
    """Method to retrieve distance between source and origin"""
    api_key = "AIzaSyBeY27HO3FB80oI60eThoWotLWQHXlHkTs"
    date = date.split("-")
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?"+ "origins=" + source +"&destinations=" + destination +"&key=" + api_key
    if ampm.lower() == "pm" : hour = str(int(hour) + 12)
    date_time = f"{date[2]}-{date[1]}-{date[0]} {hour}:{minute}:{00}"
    response = requests.get(url, timeout=100)
    distance_data = response.json()
    distance_miles = distance_data["rows"][0]["elements"][0]["distance"]["value"]/1600
    p = predict_price(distance_miles, date_time)
    cost1, cost2 = p.generate_data_return_price()
    cost = cost1 +" and " +cost2
    return cost


def create_ride(request):
    """This method processes the user request to create a new ride offering"""
    # pylint: disable=line-too-long
    initialize_database()

    if request.method == "POST":
        ride = {
            "_id": str(uuid.uuid4()),
            "source": request.POST.get("source"),
            "destination": request.POST.get("destination"),
            "ride_type": request.POST.get("ride_type"),
            "date": request.POST.get("date"),
            "hour": request.POST.get("hour"),
            "minute":  request.POST.get("minute"),
            "ampm": request.POST.get("ampm"),
            "availability": int(request.POST.get("capacity")),
            "max_size": int(request.POST.get("capacity")),
            "info": request.POST.get("info"),
            "owner": request.session["username"],
            "cost" : distance_and_cost(request.POST.get("source"), request.POST.get("destination"), request.POST.get("date"), request.POST.get("hour"), request.POST.get("minute"), request.POST.get("ampm")),
            "requested_users": [],
            "confirmed_users": []
            }

        request.session["ride"] = ride

        if rides_collection.find_one({"_id": ride["_id"]}) is None:
            rides_collection.insert_one(ride)
        # make a success dialog box or similar here.
        # return render(request, "search/search.html", {"username": request.session["username"]})

    return render(request, "publish/publish.html", {"username": request.session["username"]})

def show_ride(request, ride_id):
    """This method processes the user request to view a single ride's information"""
    initialize_database()
    ride = rides_collection.find_one({"_id": ride_id})
    return render(request, "publish/show_ride.html", {"ride_id": ride["_id"], "ride": ride})

def add_forum(request):
    """This method processes the user request to add comments in the ride's forum section"""
    if request.method == "POST":
        initialize_database()
        username = request.session["username"]
        date = datetime.now()
        content = request.POST["content"]
        ride_id = request.POST["ride"]
        post = {"user":username, "date":date, "content":content}
        rides_collection.update_one({"_id": ride_id}, {"$push": {"forum": post}})
        return redirect(show_ride, ride_id=ride_id)
