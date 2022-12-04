from django.shortcuts import render, redirect
from utils import get_client
from django.core.mail import send_mail
from django.conf import settings

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

def requested_rides(request):
    initialize_database()

    # sent requests
    sent_requests = list(rides_collection.find( { "requested_users": request.session["username"] } ))
    for ride in sent_requests:
        ride["id"] = ride["_id"]
        ride.pop("_id", None)

    # received requests
    rides_with_active_requests = list(rides_collection.find( { "owner": request.session["username"], "requested_users": { "$exists": True, "$ne": [] }} ))
    for ride in rides_with_active_requests:
        ride["id"] = ride["_id"]
        ride.pop("_id", None)

    # accepted rides
    accepted_rides = list(rides_collection.find({ "$or": [ { "owner": request.session["username"] }, { "confirmed_users": request.session["username"] } ] }))
    for ride in accepted_rides:
        ride["id"] = ride["_id"]
        ride.pop("_id", None)

    return render(request, "requests/requests.html", {"username": request.session["username"],"sent_requests": sent_requests, "received_requests": rides_with_active_requests, "accepted_rides": accepted_rides})

def cancel_ride(request, ride_id):
    initialize_database()

    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to cancel rides."
        return redirect("index")

    user = request.session["username"]

    # get ride information from db
    ride = rides_collection.find_one({"_id": ride_id})

    # remove ride request
    if user in ride["requested_users"]:
        rides_collection.update_one({"_id": ride_id}, {"$pull": {"requested_users": user}})

    return redirect(requested_rides)

def accept_request(request, ride_id, user):
    initialize_database()

    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to cancel rides."
        return redirect("index")

    # get ride information from db
    ride = rides_collection.find_one({"_id": ride_id})
    print("in1")
    # accept ride request
    if ride["availability"] > 0:
        new_availability = ride["availability"] - 1
        rides_collection.update_one({"_id": ride_id}, {"$pull": {"requested_users": user}})
        rides_collection.update_one({"_id": ride_id}, {"$push": {"confirmed_users": user}})
        rides_collection.update_one({"_id": ride_id}, {"$set": {"availability": new_availability}})
        ride_updated = rides_collection.find_one({"_id": ride_id})
        if ride_updated["availability"]==0:
            print("in")
            user=users_collection.find_one({"username" : ride["owner"]})
            body="Your ride to "+ride["destination"]+"has been booked. Please find the users below \n"
            for i in ride_updated["confirmed_users"]:
                body+=i+", " 
            subject="Ride reached capacity"
            send_capacity_mail(user['email'],body[:-2],subject)
            print("mail sent")


    return redirect(requested_rides)

def reject_request(request, ride_id, user):
    initialize_database()

    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to cancel rides."
        return redirect("index")

    # get ride information from db
    ride = rides_collection.find_one({"_id": ride_id})

    # remove ride request
    if user in ride["requested_users"]:
        rides_collection.update_one({"_id": ride_id}, {"$pull": {"requested_users": user}})

    return redirect(requested_rides)

def cancel_accepted_ride(request, ride_id, user):
    initialize_database()

    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to cancel rides."
        return redirect("index")

    # get ride information from db
    ride = rides_collection.find_one({"_id": ride_id})

    # cancel ride request
    new_availability = ride["availability"] + 1
    rides_collection.update_one({"_id": ride_id}, {"$pull": {"confirmed_users": user}})
    rides_collection.update_one({"_id": ride_id}, {"$set": {"availability": new_availability}})

    return redirect(requested_rides)

def delete_ride(request, ride_id):
    initialize_database()

    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to cancel rides."
        return redirect("index")

    # get ride information from db
    ride = rides_collection.find_one({"_id": ride_id})

    # only owner can delete ride
    if ride["owner"] == request.session["username"]:
        rides_collection.delete_one({"_id": ride_id})

    return redirect(requested_rides)
def send_capacity_mail(user_mail,body,subject):
    recepients=[user_mail]
    send_mail( subject, body, settings.EMAIL_HOST_USER, recepients)
    


