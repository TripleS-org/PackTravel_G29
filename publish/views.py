"""Django views for ride creation functionality"""
from django.http import JsonResponse
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


def get_country(location):
    """Get the country from a location using the Google Maps Geocoding API."""
    api_key = "AIzaSyC0Q5ug3tqN6lhUzknGab8sbbpsOoELkRQ"
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={api_key}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise an error for bad responses
    geocode_data = response.json()
    if geocode_data["status"] == "OK":
        # Extract the country from the address components
        for component in geocode_data["results"][0]["address_components"]:
            if "country" in component["types"]:
                return component["long_name"]
    return None



def distance_and_cost(source, destination, date, hour, minute, ampm):
    """Method to retrieve distance between source and origin"""

    source_country = get_country(source)
    destination_country = get_country(destination)

    # Check if both locations are in the same country
    if source_country != destination_country:
        return JsonResponse({"error": f"INVALID RIDE! Ride cannot be created between different countries: {source_country} and {destination_country}."}, status=400)
    api_key = "AIzaSyC0Q5ug3tqN6lhUzknGab8sbbpsOoELkRQ"
    date = date.split("-")
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?"+ "origins=" + source +"&destinations=" + destination +"&key=" + api_key
    if ampm.lower() == "pm" : hour = str(int(hour) + 12)
    date_time = f"{date[2]}-{date[1]}-{date[0]} {hour}:{minute}:{00}"

    try:
        response = requests.get(url, timeout=100)
        response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
        distance_data = response.json()

        # Check if the response contains the expected structure
        if "rows" in distance_data and len(distance_data["rows"]) > 0:
            elements = distance_data["rows"][0]["elements"]
            if len(elements) > 0 and "distance" in elements[0]:
                distance_miles = elements[0]["distance"]["value"] / 1600
                p = predict_price(distance_miles, date_time)
                cost1, cost2 = p.generate_data_return_price()
                cost = cost1 + " and " + cost2
                return cost
            else:
                raise KeyError("The 'distance' key was not found in the response.")
        else:
            raise KeyError("The response does not contain 'rows' or is empty.")
    except requests.exceptions.RequestException as e:
        return f"Error retrieving data from Google Maps API: {e}"
    except KeyError as ke:
        return f"Error processing distance data: {ke}"
#    except Exception as ex:
#        return f"An unexpected error occurred: {ex}"


def create_ride(request):
    """This method processes the user request to create a new ride offering"""
    initialize_database()

    source_country = request.POST.get("source_country")
    destination_country = request.POST.get("destination_country")

    if source_country != destination_country:
        return JsonResponse({"error": f"Rides cannot be created between different countries: {source_country} and {destination_country}."}, status=400)

    if request.method == "POST":
        source = request.POST.get("source")
        destination = request.POST.get("destination")
        # Calculate distance and cost
        cost = distance_and_cost(
            source,
            destination,
            request.POST.get("date"),
            request.POST.get("hour"),
            request.POST.get("minute"),
            request.POST.get("ampm")
        )

        # Check if cost has an error message
        if isinstance(cost, str) and cost.startswith("Error:"):
            return JsonResponse({"error": cost}, status=400)  # Return an error response

        # Prepare the ride data
        ride = {
            "_id": str(uuid.uuid4()),
            "source": source,
            "destination": destination,
            "ride_type": request.POST.get("ride_type"),
            "date": request.POST.get("date"),
            "hour": request.POST.get("hour"),
            "minute": request.POST.get("minute"),
            "ampm": request.POST.get("ampm"),
            "availability": int(request.POST.get("capacity")),
            "max_size": int(request.POST.get("capacity")),
            "info": request.POST.get("info"),
            "owner": request.session["username"],
            "cost": cost,
            "requested_users": [],
            "confirmed_users": [],
            "is_finished": False
        }

        request.session["ride"] = ride

        if rides_collection.find_one({"_id": ride["_id"]}) is None:
            rides_collection.insert_one(ride)

        return JsonResponse({"success": "Ride created successfully."}, status=201)  # Success response

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
