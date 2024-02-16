from django.urls import path
from . import views

urlpatterns = [
    path('home', views.Home, name="home"),
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
    path('send_message/', views.SendMessage, name="send_message"),
    path('edit_message/<str:pk>/', views.EditMessage, name="edit_message"),
    path('delete_message/<str:pk>/', views.DeleteMessage, name="delete_message"),
    path('send_notification/', views.SendNotification, name="send_notification"),
    path('edit_notification/<str:pk>/', views.EditNotification, name="edit_notification"),
    path('delete_notification/<str:pk>/', views.DeleteNotification, name="delete_notification"),
    path('notice/<str:pk>', views.MyNotice, name="notice"),
] 