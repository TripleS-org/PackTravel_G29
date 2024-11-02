"""Django views for user login and sign up functionality"""
from django.shortcuts import render, redirect
from utils import get_client
from .forms import RegisterForm, LoginForm, ProfileForm, FeedbackForm
import hashlib

# database connections
db_client = None
db_handle = None
users_collection = None
rides_collection = None
feedback_collection= None
user_profile = None

def initialize_database():
    """This method initializes handles to the various database collections"""
    global db_client, db_handle, users_collection, rides_collection, feedback_collection
    db_client = get_client()
    db_handle = db_client.main
    users_collection = db_handle.users
    rides_collection = db_handle.rides
    feedback_collection = db_handle.feedback

def index(request, username=None):
    """This method renders the home page of PackTravel"""
    if username is not None:
        user = username
    elif "username" not in request.session:
        user = None
    else:
        user = request.session["username"]

    if "username" in request.session:
        return render(request, "home/home.html", {"username": user})
    return render(request, "home/home.html", {"username":None})

def register(request):
    """This method processes a user registration request"""
    initialize_database()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password1"]
            username = form.cleaned_data["username"]
            user = users_collection.find_one({"username": username})
            # print(user)
            if user:
                return render(request, "user/register.html", {"form": form, "alert":"Username already exists"})
            user_obj = {
                "username": username,
                "fname": form.cleaned_data["first_name"],
                "lname": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email"],
                "password": hashlib.sha256(password.encode()).hexdigest(),
                "phone": form.cleaned_data["phone_number"],
                "rides": []
            }
            users_collection.insert_one(user_obj)
            request.session["username"] = user_obj["username"]
            request.session["fname"] = user_obj["fname"]
            request.session["lname"] = user_obj["lname"]
            request.session["email"] = user_obj["email"]
            request.session["phone"] = user_obj["phone"]
            return redirect(index, username=request.session["username"])
        else:
            print(form.errors.as_data())
    else:
        if "username" in request.session:
            return index(request)
        form = RegisterForm()
    return render(request, "user/register.html", {"form": form, "alert":""})

def logout(request):
    """This method processes user logout request"""
    try:
        request.session.clear()
    except KeyError:
        print("Exception occurred while processing logout request.")
    return redirect(index)

def login(request):
    """This method processes a login request from a user"""
    initialize_database()
    if "username" in request.session:
        return redirect(index, {"username": request.session["username"]})
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                user = users_collection.find_one({"username": username})

                if user and user["password"] == hashlib.sha256(form.cleaned_data["password"].encode()).hexdigest():
                    request.session["username"] = username
                    request.session["fname"] = user["fname"]
                    request.session["lname"] = user["lname"]
                    request.session["email"] = user["email"]
                    request.session["phone"] = user["phone"]
                    return redirect(index, request.session["username"])
                else:
                    return render(request, "user/login.html", {"form": form, "alert": "Incorrect username or password!"})

        form = LoginForm()
        return render(request, "user/login.html", {"form": form})
    

def user_profile(request): 
    initialize_database()

    username = request.session.get("username")

    if username is None:
        return redirect(login)

    user = users_collection.find_one({"username": username})

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user_data = {
                "travel_preferences": form.cleaned_data["travel_preferences"],
                "likes": form.cleaned_data["likes"],
                "is_smoker": form.cleaned_data["is_smoker"],
            }
            users_collection.update_one(
                {"username": username},  
                {"$set": user_data}     
            )
            request.session["travel_preferences"] = user_data["travel_preferences"]
            request.session["likes"] = user_data["likes"]
            request.session["is_smoker"] = user_data["is_smoker"]
            return redirect(index)
    else:
        initial_data = {
            "travel_preferences": user.get("travel_preferences", ""),
            "likes": user.get("likes", ""),
            "is_smoker": user.get("is_smoker", False)
        }
        form = ProfileForm(initial=initial_data)

    return render(request, "user/profile.html", {"form": form, "user": user})




def feedback(request, ride_id):
    """This method processes the user feedback form"""
    initialize_database()

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_data = {
                "username": request.session.get("username"),
                "ride_rating": form.cleaned_data["ride_rating"],
                "driver_rating": form.cleaned_data["driver_rating"],
                "feedback": form.cleaned_data["feedback"]
            }
            # Insert feedback into the new feedback collection
            feedback_collection.insert_one(feedback_data)
            rides_collection.update_one(
                {"_id": ride_id}, 
                {"$set": {"is_finished": True}}
            )
            return redirect(index)
    else:
        form = FeedbackForm()

    return render(request, "user/feedback.html", {"form": form})
