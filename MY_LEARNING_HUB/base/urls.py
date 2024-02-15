from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard, name="dashboard"),
    path('register', views.Register, name="register"),
    path('login', views.Login, name="login"),
    path('logout', views.Logout, name="logout"),
    path('myclass', views.MyClass, name="myclass"),
    path('todo', views.ToDo, name="todo"),
    path('about', views.About, name="about"),
    path('contact', views.Contact, name="contact"),
    path('report', views.Report, name="report"),
] 