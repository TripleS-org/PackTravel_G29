"""Django views for ride creation functionality"""
from django.shortcuts import render, redirect
from datetime import datetime
from utils import get_client
import uuid

# database connections
db_client = None
db_handle = None
users_collection = None
rides_collection  = None

def initialize_database():
    """This method initialises the handles to various database collections"""
    global db_client, db_handle, users_collection, rides_collection
    db_client = get_client()
    db_handle = db_client.main
    users_collection = db_handle.users
    rides_collection  = db_handle.rides

def publish_index(request):
    """This method processes the user request to see the publish - Create ride page"""
    initialize_database()
    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to create a ride."
        # return a meaningful message instead of simply redirecting.
        return redirect("index")
    return render(request, "publish/publish.html", {"username": request.session["username"], "alert": True})

def create_ride(request):
    """This method processes the user request to create a new ride offering"""
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
    # if request.method=="POST":
    #     username=request.session['username']
    #     date=datetime.now()
    #     content=request.POST['content']
    #     post={"user":username,"date":date,"content":content}
    #     rides_collection.update_one({"_id": route_id}, {"$push": {"forum": post}})
    ride = rides_collection.find_one({"_id": ride_id})
    return render(request,"publish/show_ride.html",{"ride_id": ride["_id"], "ride": ride})

def add_forum(request):
    """This method processes the user request to add comments in the ride's forum section"""
    if request.method=="POST":
        initialize_database()
        username=request.session["username"]
        date=datetime.now()
        content=request.POST["content"]
        ride_id=request.POST["ride"]
        post={"user":username,"date":date,"content":content}
        rides_collection.update_one({"_id": ride_id}, {"$push": {"forum": post}})
        return redirect(show_ride, ride_id=ride_id)
