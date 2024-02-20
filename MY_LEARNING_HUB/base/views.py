from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import ClassRoomForm, MessageForm, NotificationForm, TodoForm
from .models import Classroom, Notification, TODO, Message, Person, Subject
from django.contrib.auth.models import User


 
# the view that shows the current dashboard
def Home(request):
    classrooms = Classroom.objects.all()
    messages = Message.objects.all()
    notification = Notification.objects.all()
    tasks = TODO.objects.all()
    context = {"classrooms": classrooms, "messages" : messages, "notification" : notification, "tasks": tasks}
    return  render(request, 'home.html', context)

# the view for the login page
def Login(request):
    
    # if teh user is already logged in they can login again
    if request.user.is_authenticated:
        return redirect('home')
    
    # chat that teh request method is post providing some data
    if request.method == 'POST':
        # collect the specific field dates from the  form
        username =  request.POST['username'].lower()
        password =  request.POST['password']
        
        try:
            # check if the user already exists in your database by the given field
            user = User.objects.get(username=username)
        except:
            # if the user  does not exist display a message
            messages.error(request, "Username does not exist")
        # if the user does exist then go ahead and authenticate   
        user = authenticate(request, username=username, password=password)
        # finally, login te user and and return the home page
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password incorrect")
    context = {}
    return render(request, "login.html", context)

# logs you out of the session, this will be on teh nav bar
def Logout(request):
    logout(request)
    return redirect('home')


def Register(request): 
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # storing the data before we actually  save it to the database
            # making it lowercase just in case the user passed uppercase elements
           new_user = form.save(commit=False)
           new_user.username = new_user.username.lower()
           new_user.save()
           login(request,new_user)
           return redirect('home')
        else:
            messages.error(request,"Unsuccessful registration. Invalid information.")
    context = {'form': form}
    return render(request, "register.html", context)


def MyClass(request, pk):
    # create an instance of the of the specific classroom ou want to show using the pk
    classrooms = Classroom.objects.get(id=pk)
    # pass the context to be rendered on the page
    subjects = classrooms.subject_set.all()
    context = {"classrooms": classrooms, 'subjects': subjects}
    return render(request, 'class.html', context)


def MySubject(request, pk):
    # create an instance of the of the specific classroom ou want to show using the pk
    subj = Subject.objects.get(id=pk)
    messages = Message.objects.all()
    participants = subj.participants.all()
    
    if request.method == 'POST':
        new_messages = Message.objects.create(
            user = request.user,
            content = request.POST.get('body'),
            subject = subj
            
        )
        return redirect('subject', pk=subj.id)
    
    context = {"subj": subj, 'messages':messages, 'participants': participants}
    return render(request, 'subject.html', context)


def ToDo(request):
    todo = TODO.objects.all()
    context = {"todo": todo}
    return render(request, 'home.html', context)


def MyNotification(request):
    notice = Notification.objects.all()
    context = {"notice": notice}
    return render(request, 'home.html', context)


def Report(request):
    return HttpResponse("Report Page")


def About(request):
    return HttpResponse("About School Page")


def Contact(request):
    return HttpResponse("Contact Us Page")


@login_required(login_url='login')
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
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'classroom_form.html', context)


@login_required
def UpdateClassroom(request, pk):
    # create an instance of the of the specific classroom ou want to update using the pk
    room = Classroom.objects.get(id=pk)
    # use the existing instance to get the existing information you want to update
    form = ClassRoomForm(instance=room)
    
    # check if the user tying to update is the one authorized
    if request.user !=  room.class_teacher:
        return  HttpResponseForbidden("You are not authorized to edit this Classroom.")
    
    if request.method == "POST":
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            form.save()
            # on success we redirect you back to teh Home page
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'classroom_form.html', context)


@login_required
def DeleteClassroom(request, pk):
    # create an instance of the of the specific classroom ou want to delete using the pk
    room = Classroom.objects.get(id=pk)
    
    if request.user != room.class_teacher:
        return HttpResponseForbidden("You are not authorized to delete this Classroom.")
    
    if request.method == "POST":
        room.delete()
        return redirect('home')

    return render(request, 'delete_classroom.html', {'obj': room})
 

@login_required
def SendMessage(request):
    form = MessageForm
    if request.method == "POST":
        form = MessageForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'message_form.html', context)


@login_required
def EditMessage(request, pk):
    form = Message.objects.get(id=pk)
    form = MessageForm(instance=form)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'message_form.html', context)


@login_required
def DeleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    if request.method == "POST":
        message.delete()
        return redirect('home')

    return render(request, 'delete_message.html', {'obj': message})


@login_required
def SendNotification(request):
    form = NotificationForm
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'notification_form.html', context)


@login_required
def EditNotification(request, pk):
    form = Notification.objects.get(id=pk)
    form = NotificationForm(instance=form)
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'notification_form.html', context)


@login_required
def DeleteNotification(request, pk):
    notification = Notification.objects.get(id=pk)
    if request.method == "POST":
        notification.delete()
        return redirect('home')

    return render(request, 'delete_notification.html', {'obj': notification})


@login_required
def MyNotice(request, pk):
    # create an instance of the of the specific notification ou want to show using the pk
    notification = Notification.objects.get(id=pk)
    # pass the context to be rendered on the page
    context = {"notification": notification}
    return render(request, 'notice.html', context)


# this decorator means this function only works if the user is logged
@login_required
def CreateTask(request):
    form = TodoForm
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'todo_form.html', context)


@login_required
def EditTask(request, pk):
    form = TODO.objects.get(id=pk)
    form = TodoForm(instance=form)
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'todo_form.html', context)


@login_required
def DeleteTask(request, pk):
    tasks = TODO.objects.get(id=pk)
    if request.method == "POST":
        tasks.delete()
        return redirect('home')

    return render(request, 'delete_task.html', {'obj': tasks})


@login_required
def MyTask(request, pk):
    # create an instance of the of the specific notification ou want to show using the pk
    tasks = TODO.objects.get(id=pk)
    # pass the context to be rendered on the page
    context = {"tasks": tasks}
    return render(request, 'todo.html', context)
