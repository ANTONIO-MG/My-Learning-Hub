from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm
# from .models import *
# from .forms import CreateUserForm


# the view that shows the current dashboard
def Dashboard(request):
    return  HttpResponse("Dashboard Page")

# the view for the login page
def Login(request):
    return HttpResponse("Login Page")

# the view for the landing page after login

def Logout(request):
    return HttpResponse("Logout Re-direct Page")


def Register(request):
    return HttpResponse("Register Page")


def MyClass(request):
    return HttpResponse("Classroom chat Page")


def ToDo(request):
    return HttpResponse("TODO app")


def Report(request):
    return HttpResponse("Report Page")


def About(request):
    return HttpResponse("About School Page")


def Contact(request):
    return HttpResponse("Contact Us Page")
