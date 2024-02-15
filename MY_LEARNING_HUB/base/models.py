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

from django.db import models
from django.contrib.auth.models import User

# GENDER_CHOICES = [
#         ('Non', 'Non'),
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     ]
# Race = [
#         ('Asian', 'Asian'),
#         ('Black', 'Black'),
#         ('White', 'White'),
#         ('Hispanic', 'Hispanic'),
#         ('Other', 'Other'),
#     ]
# Notification_Groups = [
#     ('educators', 'educators'),
#     ('students', 'students'),
#     ('all', 'all'),
# ]

TASK_STATUS = [
    (0, "Not Started"),  # Not started yet
    (1, "In Progress"),   # Currently working on it
    (2, "Completed"),      # Finished
]


class Classroom(models.Model):
    name = models.CharField(max_length=255)
    class_teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering  = ['-created_at', '-created_at']

    def __str__(self):
        return str(self.name)
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_room = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-created_at']

    def __str__(self):
        return str(self.content[0:50])
    
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-created_at']

    def __str__(self):
        return str(self.title)
    

class TODO(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at', '-created_at']

    def __str__(self):
        return str(self.title)
