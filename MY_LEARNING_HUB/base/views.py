from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import ClassRoomForm
from .models import Classroom, Notification, TODO, Message
# from .forms import CreateUserForm


 

# the view that shows the current dashboard
def Dashboard(request):
    classrooms = Classroom.objects.all()
    context = {"classrooms": classrooms}
    return  render(request, 'dashboard.html', context)

# the view for the login page
def Login(request):
    return HttpResponse("Login Page")

# the view for the landing page after login

def Logout(request):
    return HttpResponse("Logout Re-direct Page")


def Register(request):
    return HttpResponse("Register Page")


def MyClass(request, pk):
    # create an instance of the of the specific classroom ou want to show using the pk
    classrooms = Classroom.objects.get(id=pk)
    # pass the context to be rendered on teh page
    context = {"classrooms": classrooms}
    return render(request, 'class.html', context)


def ToDo(request):
    classrooms = Classroom.objects.all()
    context = {"classrooms": classrooms}
    return HttpResponse("TODO app")


def Report(request):
    return HttpResponse("Report Page")


def About(request):
    return HttpResponse("About School Page")


def Contact(request):
    return HttpResponse("Contact Us Page")

def CreateClassroom(request):
    # create an instance of the of the specific classroom
    form = ClassRoomForm
    # check if the method being returned by the url and the form on teh HTML is post
    if request.method == "POST":
        # if it's  a POST request we populate the instance with data from the form request
        form = ClassRoomForm(request.POST)
        # if form is valid we go ahead and save all the data into the database
        if  form.is_valid():
            form.save()
            # on success we redirect you back to teh Home page
            return redirect('dashboard')
    
    context = {'form': form}
    return render(request, 'classroom_form.html', context)

def UpdateClassroom(request, pk):
    # create an instance of the of the specific classroom ou want to update using the pk
    form = Classroom.objects.get(id=pk)
    # use the existing instance to get the existing information you want to update
    form = ClassRoomForm(instance=form)
    if request.method == "POST":
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            form.save()
            # on success we redirect you back to teh Home page
            return redirect('dashboard')
    
    context = {'form': form}
    return render(request, 'classroom_form.html', context)


def DeleteClassroom(request, pk):
    # create an instance of the of the specific classroom ou want to delete using the pk
    room = Classroom.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('dashboard')

    return render(request, 'delete.html', {'obj': room})
 