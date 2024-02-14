from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .email_back_end import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
# from django.core.checks import messages
from django.contrib import messages


# the view that shows the current da   shboard
def showDashboard(request):
    return  render(request, 'home.html')

# the view for the login page
def loginPage(request):
    return  render(request,'login.html')

# the view for the landing page after login
def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>NOT ALLOWED</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            return render(request, 'home.html')
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")

def  logoutUser(request):
    pass

# function that returns the logged in user details
def getUserDetails(request):
    if request.user != None:
        return HttpResponse("User : "+request.user.email+" usertype : "+" Password : "+request.user.user_type)
    else:
        return HttpResponse("Please Login first")

# logs out the current user
def logOut(request):
    logout(request)
    return HttpResponseRedirect("/")

def baseHtml(request):
    return  render(request,"home.html")

# the adding secction with forms
def addEducator(request):
    return  render(request, "add_educator.html")

def addStudent(request):
    return render(request, "add_student.html")

def addCourse(request):
    return render(request, "add_course.html")
