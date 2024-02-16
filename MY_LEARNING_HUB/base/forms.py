from django.forms import  ModelForm
from .models import Classroom, Message, Notification, TODO

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
