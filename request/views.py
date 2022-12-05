"""Django views for ride management functionality"""
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from utils import get_client

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

def requested_rides(request):
    """This method processes the request to render the list of rides requested by the user, rides waiting approval and confirmed rides"""
    initialize_database()

    # sent requests
    sent_requests = list(rides_collection.find({ "requested_users": request.session["username"]} ))
    for ride in sent_requests:
        ride["id"] = ride["_id"]
        ride.pop("_id", None)

    # received requests
    rec_req = list(rides_collection.find({ "owner": request.session["username"], "requested_users": { "$exists": True, "$ne": [] }}))
    for ride in rec_req:
        ride["id"] = ride["_id"]
        ride.pop("_id", None)

    # accepted rides
    accepted_rides = list(rides_collection.find({ "$or": [ { "owner": request.session["username"] }, { "confirmed_users": request.session["username"] }]}))
    for ride in accepted_rides:
        ride["id"] = ride["_id"]
        ride.pop("_id", None)

    data = {"username": request.session["username"], "sent_requests": sent_requests, "received_requests": rec_req, "accepted_rides": accepted_rides}
    return render(request, "requests/requests.html", data)

def cancel_ride(request, ride_id):
    """This method processes the user request to cancel a ride request before it gets confirmed"""
    initialize_database()

    if "username" not in request.session:
        request.session["alert"] = "Please login to cancel rides."
        return redirect("index")

    user = request.session["username"]

    # get ride information from db
    ride = rides_collection.find_one({"_id": ride_id})

    # remove ride request
    if ride is not None and user in ride["requested_users"]:
        rides_collection.update_one({"_id": ride_id}, {"$pull": {"requested_users": user}})

    return redirect(requested_rides)

def accept_request(request, ride_id, user):
    """This method processes the ride owner's request to accept a rider"""
    initialize_database()

    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to cancel rides."
        return redirect("index")

    # get ride information from db
    ride = rides_collection.find_one({"_id": ride_id})
    print("in1")
    # accept ride request
    if ride is not None and ride["availability"] > 0:
        new_availability = ride["availability"] - 1
        insert_data = {"$pull": {"requested_users": user}, "$push": {"confirmed_users": user}, "$set": {"availability": new_availability}}
        rides_collection.update_one({"_id": ride_id}, insert_data)
        ride_updated = rides_collection.find_one({"_id": ride_id})
        if ride_updated["availability"]==0:
            print("in")
            user = users_collection.find_one({"username" : ride["owner"]})
            body = "Your ride to " + ride["destination"] + "has been booked. Please find the users below \n"
            for i in ride_updated["confirmed_users"]:
                body += i+", "
            subject = "Ride reached capacity"
            send_capacity_mail(user["email"],body[:-2],subject)
            print("mail sent")


    return redirect(requested_rides)

def reject_request(request, ride_id, user):
    """This method processes the ride owner's request to reject a rider"""
    initialize_database()

    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to cancel rides."
        return redirect("index")

    # get ride information from db
    ride = rides_collection.find_one({"_id": ride_id})

    # remove ride request
    if ride is not None and user in ride["requested_users"]:
        rides_collection.update_one({"_id": ride_id}, {"$pull": {"requested_users": user}})

    return redirect(requested_rides)

def cancel_accepted_ride(request, ride_id, user):
    """This method processes user request to cancel an accepted ride"""
    initialize_database()

    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to cancel rides."
        return redirect("index")

    # get ride information from db
    ride = rides_collection.find_one({"_id": ride_id})

    # cancel ride request
    if ride is not None:
        new_availability = ride["availability"] + 1
        rides_collection.update_one({"_id": ride_id}, {"$pull": {"confirmed_users": user}, "$set": {"availability": new_availability}})

    return redirect(requested_rides)

def delete_ride(request, ride_id):
    """This method processes ride owner request to delete a ride"""
    initialize_database()

    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to cancel rides."
        return redirect("index")

    # get ride information from db
    ride = rides_collection.find_one({"_id": ride_id})

    # only owner can delete ride
    if ride is not None and ride["owner"] == request.session["username"]:
        rides_collection.delete_one({"_id": ride_id})

    return redirect(requested_rides)

def send_capacity_mail(user_mail,body,subject):
    """Method to send email"""
    recepients = [user_mail]
    send_mail( subject, body, settings.EMAIL_HOST_USER, recepients)
