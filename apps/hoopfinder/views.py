from django.shortcuts import render, redirect

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
    return render(request, "hoopfinder/courts.html")

def registration(request):
    return render(request, "hoopfinder/registration.html")

def login(request):
    return render(request, "hoopfinder/login.html")

def new_court(request):
    return render(request, "hoopfinder/new_court.html")

def add_court(request):
    if request.method == 'POST':
        print("aaaA")
    return redirect('/courts')

