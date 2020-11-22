from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print("Here")
    return render(request,'portal.html')

def portal(request):
    return render(request, 'portal.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    user.is_teacher= True
    return render(request, 'dashboard.html')

def signup(request):
    return render(request, 'signup.html')

def class_students(request):
    return render(request, 'class_students.html')

