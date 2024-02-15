from django.forms import  ModelForm
from .models import Classroom

class  ClassRoomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'