from django.shortcuts import render, redirect
from .models import *
import json
import requests

# Create your views here.

def index(request):
    return render(request, "hoopfinder/landing.html")

def home(request):
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

def login(request):
    return render(request, "hoopfinder/login.html")

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
