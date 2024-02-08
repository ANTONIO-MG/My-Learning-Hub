from django.contrib import admin

# Register your models here.
from base.models import CustomUser

from django.contrib.auth.admin import UserAdmin

class userModel(UserAdmin):
    pass 

# authenticating the CustomUser for session control
admin.site.register(CustomUser, userModel)
