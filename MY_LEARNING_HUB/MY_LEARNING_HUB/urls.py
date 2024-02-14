"""
URL configuration for MY_LEARNING_HUB project.

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from base import views
from MY_LEARNING_HUB import settings

# added the static files to be able to load the files under the static folder
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.showDashboard),
    path('', views.loginPage),
    path('DoLogin', views.doLogin),
    path('get_user_details', views.getUserDetails),
    path('logout_user', views.logOut),
    path('base', views.baseHtml),
    path('add_educator', views.addEducator),
    path('add_student', views.addStudent),
    path('add_course', views.addCourse),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)