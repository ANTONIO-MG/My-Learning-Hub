from django.db import models
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


class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    student_number = models.CharField(max_length=20, unique=True)
    race = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    id_number = models.CharField(max_length=13, unique=True)
    contact_number = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=15)
    home_language = models.CharField(max_length=50)
    merits = models.PositiveIntegerField()
    disability = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20)
    parents = models.ManyToManyField('Parent', related_name='children')
    reports = models.ManyToManyField('Report', related_name='students')
    profile_picture = models.ImageField(
        upload_to='profile_pics/', null=True, blank=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Educator(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    staff_number = models.CharField(max_length=20, unique=True)
    race = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    id_number = models.CharField(max_length=13, unique=True)
    contact_number = models.CharField(max_length=15)
    home_language = models.CharField(max_length=50)
    disability = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', null=True, blank=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Admin_HOD(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    staff_number = models.CharField(max_length=20, unique=True)
    id_number = models.CharField(max_length=13, unique=True)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Parent(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    id_number = models.CharField(max_length=13, unique=True)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', null=True, blank=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Report(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE)
    summary = models.TextField(blank=True, null=True)
    grades_list = models.JSONField(blank=True, null=True)
    picture = models.ImageField(upload_to='report_pics/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

