from django import forms
from django.forms import  ModelForm
from .models import Classroom, Message, Notification, TODO, Person

# form to create a classroom
class  ClassRoomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'
        
# form to create a message
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        
    # def __init__(self, *args, **kwargs):
    #     super(MessageForm, self).__init__(*args, **kwargs)
    #     # Exclude specific fields
    #     exclude_fields = ['subject', 'subjects', 'user', 'class_room']
    #     for field_name in exclude_fields:
    #         if field_name in self.fields:
    #             del self.fields[field_name]

# form to create a Notification
class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'

# form to create a task
class TodoForm(ModelForm):
    class Meta:
        model = TODO
        fields = '__all__'


class EditProfileForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ['last_name', 'gender',
                   'race', 'emergency_contact',
                   'is_staff', 'is_active',
                   'groups', 'last_login', 'subjects',
                   'user_permissions', 'is_superuser']
        

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ['profile_picture',
                   'user_category', 'last_name', 'gender',
                   'race', 'emergency_contact', 'profile_picture',
                   'is_staff', 'is_active', 'date_of_birth', 'first_name',
                   'groups', 'superuser', 'last_login', 'subjects',
                   'user_permissions', 'is_superuser']
    my_class = forms.ModelChoiceField(
        queryset=Classroom.objects.all(), required=False)
