from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ClassRoomForm, MessageForm, NotificationForm, TodoForm
from .models import Classroom, Notification, TODO, Message
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
    # chat that teh request method is post providing some data
    if request.method == 'POST':
        # collect the specific field dates from the  form
        username =  request.POST['username']
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
    return render(request, "login_register.html", context)

# logs you out of the session, this will be on teh nav bar
def Logout(request):
    logout(request)
    return redirect('home')


def Register(request):
    return HttpResponse("Register Page")


def MyClass(request, pk):
    # create an instance of the of the specific classroom ou want to show using the pk
    classrooms = Classroom.objects.get(id=pk)
    # pass the context to be rendered on the page
    context = {"classrooms": classrooms}
    return render(request, 'class.html', context)


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
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'classroom_form.html', context)


def DeleteClassroom(request, pk):
    # create an instance of the of the specific classroom ou want to delete using the pk
    room = Classroom.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')

    return render(request, 'delete_classroom.html', {'obj': room})
 
 
def SendMessage(request):
    form = MessageForm
    if request.method == "POST":
        form = MessageForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'message_form.html', context)

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


def DeleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    if request.method == "POST":
        message.delete()
        return redirect('home')

    return render(request, 'delete_message.html', {'obj': message})


def SendNotification(request):
    form = NotificationForm
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'notification_form.html', context)


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


def DeleteNotification(request, pk):
    notification = Notification.objects.get(id=pk)
    if request.method == "POST":
        notification.delete()
        return redirect('home')

    return render(request, 'delete_notification.html', {'obj': notification})


def MyNotice(request, pk):
    # create an instance of the of the specific notification ou want to show using the pk
    notification = Notification.objects.get(id=pk)
    # pass the context to be rendered on the page
    context = {"notification": notification}
    return render(request, 'notice.html', context)


# ------------------------------------>

def CreateTask(request):
    form = TodoForm
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'todo_form.html', context)


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


def DeleteTask(request, pk):
    tasks = TODO.objects.get(id=pk)
    if request.method == "POST":
        tasks.delete()
        return redirect('home')

    return render(request, 'delete_task.html', {'obj': tasks})


def MyTask(request, pk):
    # create an instance of the of the specific notification ou want to show using the pk
    tasks = TODO.objects.get(id=pk)
    # pass the context to be rendered on the page
    context = {"tasks": tasks}
    return render(request, 'todo.html', context)
