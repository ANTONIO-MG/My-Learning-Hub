""" models that represent the data for each user and function of the management application

Course:
    Represents an academic course or grade the student is at.
    This will have 
Fields:
    created_at: Date and time when the course was created.
    updated_at: Date and time when the course was last updated.
    
Student:
    Represents a student enrolled in the system.
Fields:
name: First name of the student.
surname: Last name of the student.
gender: Gender of the student.
student_number: Unique identifier for the student.
race: Race of the student.
citizenship: Citizenship status of the student.
date_of_birth: Date of birth of the student.
id_number: Unique national ID number of the student.
contact_number: Contact number for the student.
emergency_contact: Emergency contact number for the student.
home_language: Home language of the student.
merits: Merit points earned by the student.
disability: Disability status of the student.
status: Academic status of the student.
parents: Many-to-many relationship with Parent model.
reports: Many-to-many relationship with Report model.
profile_picture: Profile picture of the student.
password: Password for student login.
created_at: Date and time when the student was created.
updated_at: Date and time when the student was last updated.
course: Foreign key relation to the Course model.


Educator:
    Represents an educator or teacher.
Fields:
name: First name of the educator.
surname: Last name of the educator.
gender: Gender of the educator.
staff_number: Unique identifier for the educator.
race: Race of the educator.
citizenship: Citizenship status of the educator.
date_of_birth: Date of birth of the educator.
id_number: Unique national ID number of the educator.
contact_number: Contact number for the educator.
home_language: Home language of the educator.
disability: Disability status of the educator.
email: Email address of the educator.
profile_picture: Profile picture of the educator.
password: Password for educator login.
created_at: Date and time when the educator was created.
updated_at: Date and time when the educator was last updated.

4. Admin_HOD:
    Represents a Head of Department (HOD) administrator.
Fields:
name: First name of the HOD.
surname: Last name of the HOD.
staff_number: Unique identifier for the HOD.
id_number: Unique national ID number of the HOD.
contact_number: Contact number for the HOD.
email: Email address of the HOD.
profile_picture: Profile picture of the HOD.
password: Password for HOD login.
created_at: Date and time when the HOD was created.
updated_at: Date and time when the HOD was last updated.

Parent:
     Represents a parent or guardian of a student.
Fields:
name: First name of the parent.
surname: Last name of the parent.
gender: Gender of the parent.
id_number: Unique national ID number of the parent.
contact_number: Contact number for the parent.
email: Email address of the parent.
profile_picture: Profile picture of the parent.
password: Password for parent login.
created_at: Date and time when the parent was created.
updated_at: Date and time when the parent was last updated.

Subject:
    Represents an academic subject.
Fields:
subject_name: Name of the subject.
course: Foreign key relation to the Course model.
educator: Foreign key relation to the Educator model.
created_at: Date and time when the subject was created.
updated_at: Date and time when the subject was last updated.

Notification:
    Represents a notification sent to a student.
Fields:
student: Foreign key relation to the Student model.
course: Foreign key relation to the Course model.
educator: Foreign key relation to the Educator model.
message:

"""

# bellow are the list of classes that map data to teh database

from django.utils import timezone
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
Race = [
        ('Asian', 'Asian'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Hispanic', 'Hispanic'),
        ('Other', 'Other'),
    ]
Notification_Groups = [
    ('educators', 'Educators'),
    ('students', 'Students'),
    ('all', 'All'),
]

USER_TYPE_CHOICES = [
    ('student', 'Student'),
    ('educator', 'Educator'),
    ('parent', 'Parent'),
    ('staff', 'Staff'),
]


class PersonManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)


class Person(AbstractBaseUser, PermissionsMixin):
    objects = PersonManager()
    user_name = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=50, default="first name")
    last_name = models.CharField(max_length=50, default="last name")
    email = models.EmailField(unique=True, blank=True,
                              null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    bio = models.TextField(max_length=500, blank=True) 
    my_class = models.ForeignKey(
        'Classroom', on_delete=models.SET_NULL, null=True, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES,
        default='Student')
    race = models.CharField(
        max_length=50, choices=Race, default='Other')
    date_of_birth = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=15)
    subjects = models.ManyToManyField('Subject', blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # makes the email field teh default base field
    USERNAME_FIELD = 'email'
    # created the fields tha are required at user creation stage
    REQUIRED_FIELDS = ['user_name']
    
    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return str(self.user_name)


class Classroom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    participants =models.ManyToManyField(
        Person, blank=True)
    subjects = models.ManyToManyField('Subject',  blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering  = ['-updated_at', '-created_at']

    def __str__(self):
        return str(self.name)
    
class Message(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    subject = models.ForeignKey(
        'Subject', null=True, blank=True, on_delete=models.CASCADE)
    class_room = models.ForeignKey(
        Classroom, null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return str(self.content[0:50])
    
    
class Notification(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    notification_group = models.CharField(
        max_length=25, choices=Notification_Groups, default='All')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return str(self.title)
    



class Subject(models.Model):
    room = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    participants = models.ManyToManyField(
        Person, related_name='participants', blank=True)
    teacher = models.ForeignKey(
        Person, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return str(self.title)
    
  
class TODO(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    task_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return str(self.title)

  
class TaskCompletion(models.Model):
    user = models.ForeignKey('Person', on_delete=models.CASCADE)
    task = models.ForeignKey(TODO, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    completion_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return f'{self.user} - {self.task}'
    
class Post(models.Model):
    user = models.ForeignKey('Person', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    post_body = models.TextField(blank=True, null=True)
    picture = models.ImageField(
        upload_to='profile_pics/', null=True, blank=True)
    media = models.FileField(upload_to='audio_files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return f'{self.title} - {self.user  }'
