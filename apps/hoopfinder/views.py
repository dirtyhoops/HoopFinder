from django.shortcuts import render, redirect
from .models import *
import json
import requests

# Create your views here.

# MAKE AN EDIT USER page
# MAKE SURE THE DATABASE IS ALL CONNECTED TO EACH OTHER
# MAKE SURE THE THEME IS ALL GOOD TO GO BY FRIDAY MORNING

def index(request):
    return render(request, "hoopfinder/landing.html")

def home(request):
    if 'userid' not in request.session:
        request.session['userid'] = 0
    return render(request, "hoopfinder/main.html")

def map(request):
    return render(request, "hoopfinder/maps.html")
    
def userdashboard(request):
    return render(request, "hoopfinder/user_dashboard.html")

def courts(request):
    all_courts = Courts.objects.all()
    context = {
        "all_courts": all_courts
    }
    return render(request, "hoopfinder/courts.html", context)

def registration(request):
    return render(request, "hoopfinder/registration.html")

def register(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/registration')
        else:
            request.session['first_name'] = request.POST['first_name']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']

            #BCRYPT
            pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            confpassword = request.POST['confpassword']
           
            #create an account and push it to the database
            user2 = User.objects.create(first_name = first_name, last_name =last_name, email = email, password = pw)
            request.session['userid'] = user2.id
            
            # change this to userdashboard
            return redirect('/home')


def login(request):
    return render(request, "hoopfinder/login.html")

def login_post(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST) 
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user1 = User.objects.get(email=request.POST['email'])
            request.session['userid'] = user1.id
            # change this to user dashboard
            print("youre logged in " + user1.first_name)
            return redirect('/home')

def new_court(request):
    return render(request, "hoopfinder/new_court.html")

def add_court(request):
    if request.method == 'POST':
        name = request.POST['court_name']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        imagelink = request.POST['imagelink']        ######change this to a real file upload later##########

        Courts.objects.create(name = name, address = address, city = city, state = state, zipcode = zipcode, imagelink = imagelink)
        print("1 court is added")
    return redirect('/courts')

def show_court(request, id):
    court = Courts.objects.get(id = id)
    api_address = "http://api.openweathermap.org/data/2.5/weather?appid=49a76676e913deb3805b87568bba047f&zip="+ court.zipcode
    json_data = requests.get(api_address).json()
    temperature = json_data['main']['temp']
    ftemperature = (temperature*9)/5 - 459.67
    context = {
        # "city": json_data['sys'][0]['name'],
        "ftemperature": ftemperature,
        "description": json_data['weather'][0]['description'],
        "icon": json_data['weather'][0]['icon'],
        "court": court
    }

    return render(request, "hoopfinder/show_court.html", context)