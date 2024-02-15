from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.Dashboard, name="dashboard"),
    path('register', views.Register, name="register"),
    path('login', views.Login, name="login"),
    path('logout', views.Logout, name="logout"),
    path('class/<str:pk>', views.MyClass, name="class"),
    path('todo', views.ToDo, name="todo"),
    path('about', views.About, name="about"),
    path('contact', views.Contact, name="contact"),
    path('report', views.Report, name="report"),
    path('create_classroom/', views.CreateClassroom, name="create_classroom"),
    path('update_classroom/<str:pk>/', views.UpdateClassroom, name="update_classroom"),
    path('delete_classroom/<str:pk>/', views.DeleteClassroom, name="delete_classroom"),
] 