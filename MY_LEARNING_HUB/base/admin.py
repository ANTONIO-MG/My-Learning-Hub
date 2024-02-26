from django.contrib import admin
from .models import Classroom, Notification, Message, TODO, Person, Subject, TaskCompletion, Post

admin.site.register(Classroom)
admin.site.register(Notification)
admin.site.register(Message)
admin.site.register(TODO)
admin.site.register(Person)
admin.site.register(Subject)
admin.site.register(TaskCompletion)
admin.site.register(Post)
