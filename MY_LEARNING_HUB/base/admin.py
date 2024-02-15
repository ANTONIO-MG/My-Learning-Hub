from django.contrib import admin
from .models import Classroom, Notification, Message, TODO

admin.site.register(Classroom)
admin.site.register(Notification)
admin.site.register(Message)
admin.site.register(TODO)
