"""" 
Function based vies for the base app, the base app is the application running all
User, Tasks, Notifications, Messages, Classrooms, Subjects CRUD (create, read, update, Delete) functions
This also manages the database sessions and data management
"""

# the imports
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import ClassRoomForm, MessageForm, NotificationForm, TodoForm, PersonForm, EditProfileForm, PostForm, PersonEditForm
from .models import Classroom, Notification, TODO, Message, Person, Subject, TaskCompletion, Post
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


 
# The homepage view
def Home(request):
    """
    classroom: stores all the classroom as objects and can be queried
    messages: stores all the messages on teh database and can be queried
    """
    date = timezone.now()
    today = date.strftime('%Y-%m-%d')
    
    classrooms = Classroom.objects.all()
    messages = Message.objects.all()
    notifications = Notification.objects.all()[0:3]
    tasks = TODO.objects.all()
    all_users = Person.objects.all()
    assigned_task = TaskCompletion.objects.filter(user=request.user)
    subjects = Subject.objects.all()
    me = Person.objects.get(id=request.user.pk)
    my_class = request.user.my_class
    print(my_class)
    context = {"classrooms": classrooms, "messages" : messages,
               "notifications" : notifications, "tasks": tasks,
               "subjects": subjects, 'my_class': my_class,
               'all_users': all_users, 'assigned_task': assigned_task,
               'today': today}
    return  render(request, 'home.html', context)


def Profile(request, pk):
    me = Person.objects.get(id=pk)
    all_posts = Post.objects.all()
    all_users = Person.objects.all()
    subjects = me.participants.all()
    classrooms = Classroom.objects.all()
    messages = Message.objects.all()
    notifications = Notification.objects.all()[0:5]
    my_class = request.user.my_class
    tasks = TODO.objects.all()
    context = {"classrooms": classrooms, "messages": messages,
               "notifications": notifications, "tasks": tasks,
               'me':me, 'subjects': subjects,
               'all_users': all_users, 'all_posts': all_posts, 'my_class': my_class, }
    return render(request, 'profile.html', context)


def EditProfile(request, pk):
    person = Person.objects.get(id=pk)
    form = PersonEditForm(instance=person)
    if request.method == "POST":
        form = PersonEditForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'edit_profile.html', context)

# the view for the login page


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # Collect the specific field dates from the form
        email = request.POST['email'].lower()
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Check if the user is active
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Your account is not active.")
        else:
            messages.error(request, "Invalid email or password.")

    context = {}
    return render(request, "login.html", context)

# logs you out of the session, this will be on teh nav bar
def Logout(request):
    logout(request)
    return redirect('login')


def Register(request): 
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            login(request, new_user)
            pk = new_user.id

            # Assuming you have a field in your Person model to store the selected class
            selected_class = new_user.my_class

            # Add the new user as a participant to all the subjects of the selected class
            subjects_for_class = selected_class.subjects.all()
            for subject in subjects_for_class:
                subject.participants.add(new_user)

            # Add the new user as a participant to the participants of the selected class
            selected_class.participants.add(new_user)

            return redirect('edit_profile', pk)
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")

    context = {'form': form}
    return render(request, "register.html", context)


def MyClass(request, pk):
    # create an instance of the of the specific classroom ou want to show using the pk
    classroom = Classroom.objects.get(id=pk)
    # pass the context to be rendered on the page
    subjects = Classroom.objects.all()
    participants = classroom.participants.all()
    posts = Post.objects.all()
    
    if request.method == 'POST':
        new_post = Post.objects.create(
            user=request.user,
            title=request.POST.get('post_title'),
            post_body=request.POST.get('content'),

        )
        return redirect('subject', pk=classroom.id)
    
    context = {"classroom": classroom, 'subjects': subjects,
               'participants': participants, 'posts': posts}
    return render(request, 'class.html', context)


def MySubject(request, pk):
    subj = Subject.objects.get(id=pk)
    messages = Message.objects.all()
    people = Person.objects.all()
    person = Person.objects.get(id=request.user.id)
    participants = subj.participants.all()
    classroom = Classroom.objects.get(id=subj.room.id)  # Corrected line

    if request.method == 'POST':
        new_message = Message.objects.create(
            user=request.user,
            content=request.POST.get('message'),  # Corrected line
            subject=subj,
            class_room =subj.room
        )
        return redirect('subject', pk=subj.id)

    context = {"subj": subj, 'messages': messages,
               'participants': participants, 'classroom': classroom,
               'people': people, 'person': person}
    return render(request, 'subject.html', context)


def ToDo(request):
    todo = TODO.objects.all()
    context = {"todo": todo}
    return render(request, 'home.html', context)


def MyNotification(request):
    notice = Notification.objects.all()
    context = {"notice": notice}
    return render(request, 'home.html', context)


def Report(request):
    return HttpResponse("Report Page")


def About(request):
    return HttpResponse("About School Page")


def ContactUs(request):
    return render (request, "contact.html", {})


@login_required()
def CreateClassroom(request):
    
    create = True
    # create an instance of the of the specific classroom
    form = ClassRoomForm
    # check if the method being returned by the url and the form on teh HTML is post
    all_subjects = Subject.objects.all()
    all_students = Person.objects.all()
    
    if request.method == 'POST':
        new_post = Post.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            post_body=request.POST.get('post'),
            picture=request.POST.get('post_picture'),
            media=request.POST.get('post_media'),

        )
        return redirect('home')
    
    context = {'form': form, 'create': create,
               'all_subjects': all_subjects, 'all_students': all_students}
    return render(request, 'classroom_form.html', context)


@login_required
def UpdateClassroom(request, pk):
    create = False
    room = Classroom.objects.get(id=pk)

    # Check if the user trying to update is authorized
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to edit this Classroom.")

    if request.method == "POST":
        form = ClassRoomForm(request.POST, instance=room)
        if form.is_valid():
            # Delete the existing instance
            room.delete()

            # Save the updated form as a new instance
            new_instance = form.save(commit=False)
            new_instance.id = pk  # Set the id to the original id
            new_instance.save()

            # Redirect to the Home page on success
            return redirect('home')
    else:
        form = ClassRoomForm(instance=room)

    context = {'form': form, 'create': create}
    return render(request, 'classroom_form.html', context)


@login_required
def DeleteClassroom(request, pk):
    # create an instance of the of the specific classroom ou want to delete using the pk
    room = Classroom.objects.get(id=pk)
    
    if request.user.is_superuser != True:
        return HttpResponseForbidden("You are not authorized to delete this Classroom.")
    
    if request.method == "POST":
        room.delete()
        return redirect('home')

    return render(request, 'delete_classroom.html', {'obj': room})
 

@login_required
def SendMessage(request):
    create = True
    form = MessageForm
    form.user =  request.user
    if request.method == "POST":
        form = MessageForm(request.POST)
        if  form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            return redirect('home')
    
    context = {'form': form, 'create': create}
    return render(request, 'message_form.html', context)


@login_required
def EditMessage(request, pk):
    
    create = False
    message = get_object_or_404(Message, id=pk)
    form = Message.objects.get(id=pk)
    form = MessageForm(instance=form)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            message.delete()
            return redirect('home')
    
    context = {'form': form, 'create': create}
    return render(request, 'message_form.html', context)


@login_required
def DeleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    
    if request.user != message.user:
        return HttpResponse("Not Allowed to delete")
    
    if request.method == "POST":
        message.delete()
        return redirect('subject', pk=message.subject.id)

    return render(request, 'delete_message.html', {'obj': message})


@login_required
def SendNotification(request):
    form = NotificationForm
    if request.method == "POST":
        form = NotificationForm(request.POST)
        
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'notification_form.html', context)


@login_required
def EditNotification(request, pk):
    create = False
    note = get_object_or_404(Notification, id=pk)

    if request.method == "POST":
        form = NotificationForm(request.POST, instance=note)
        if form.is_valid():
            # Delete the existing post
            note.delete()

            # Save the updated post
            form.instance.user = request.user
            new_instance = form.save()

            return redirect('home')
    else:
        form = NotificationForm(instance=note)

    context = {'form': form, 'create': create}
    return render(request, 'notification_form.html', context)


@login_required
def DeleteNotification(request, pk):
    notification = Notification.objects.get(id=pk)
    if request.method == "POST":
        notification.delete()
        return redirect('home')

    return render(request, 'delete_notification.html', {'obj': notification})

def MyNotification(request, pk):
    notification = Notification.objects.get(id=pk)
    context = {'notification': notification}
    return render(request, 'notification.html', context)


@login_required
def MyNotice(request, pk):
    # create an instance of the of the specific notification ou want to show using the pk
    notification = Notification.objects.get(id=pk)
    # pass the context to be rendered on the page
    context = {"notification": notification}
    return render(request, 'notice.html', context)


# this decorator means this function only works if the user is logged
@login_required
def CreateTask(request):
    create = True
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            # Save the task
            form.instance.user = request.user
            task = form.save()

            # Automatically add the task to all participants in the selected subject(s)
            selected_subject = form.cleaned_data['subject']
            participants = selected_subject.participants.all()

            
            for participant in participants:
                 # Create TaskCompletion for each participant
                TaskCompletion.objects.create(
                user=participant,
                    task=task,
            )
            return redirect('home')
    else:
        form = TodoForm()

    context = {'form': form, 'create': create}
    return render(request, 'todo_form.html', context)


@login_required
def EditTask(request, pk):
    create = False
    # Get the original task
    original_task = TODO.objects.get(id=pk)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=original_task)
        if form.is_valid():
            # Delete the original task
            original_task.delete()

            # Create a new task with updated information
            new_task = form.save(commit=False)
            new_task.created_at = original_task.created_at  # Keep the original creation date
            new_task.updated_at = timezone.now()  # Update the updated date to now
            new_task.save()

            return redirect('home')
    else:
        form = TodoForm(instance=original_task)

    context = {'form': form, 'create': create}
    return render(request, 'todo_form.html', context)


@login_required
def DeleteTask(request, pk):
    tasks = TODO.objects.get(id=pk)
    if request.method == "POST":
        tasks.delete()
        return redirect('home')

    return render(request, 'delete_task.html', {'obj': tasks})


@login_required
def MyTask(request, pk):
    # create an instance of the of the specific notification ou want to show using the pk
    tasks = TaskCompletion.objects.get(id=pk)
    subject_task = TODO.objects.get(title=tasks.task)
    # pass the context to be rendered on the page
    context = {"tasks": tasks, 'subject_task': subject_task}
    return render(request, 'todo.html', context)


@login_required
def CreatePost(request):
    
    create = True
    
    form = PostForm(request.POST)

    if request.method == 'POST':
        new_post = Post.objects.create(
            user = request.user,
            title = request.POST.get('title'),
            post_body = request.POST.get('post'),
            picture = request.POST.get('post_picture'),
            media = request.POST.get('post_media'),
            
        )
        return redirect('home')
    context = {'form': form, 'create': create}

    return render(request, 'post_form.html', context)



@login_required
def EditPost(request, pk):
    
    create = False
    # Get the original task
    original_post = Post.objects.get(id=pk)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=original_post)
        if form.is_valid():
            # Delete the original post
            original_post.delete()

            # Create a new task with updated information
            new_post = form.save(commit=False)
            new_post.created_at = original_post.created_at  # Keep the original creation date
            new_post.updated_at = timezone.now()  # Update the updated date to now
            new_post.save()

            return redirect('home')
    else:
        form = PostForm(instance=original_post)

    context = {'form': form, 'create': create}
    return render(request, 'post_form.html', context)


@login_required
def DeletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'delete_post.html', {'obj': post})


@login_required
def MyPost(request, pk):
    post = Post.objects.get(id=pk)

    return render(request, 'delete_task.html', {'obj': post})


def MySubjects(request):
    
    me = Person.objects.get(id=request.user.pk)
    subjects = Subject.objects.all()
    my_class = request.user.my_class
    context = {'subjects': subjects, 'my_class': my_class}
    return render(request, 'my_subjects.html', context)


def MyNotifications(request):

    me = Person.objects.get(id=request.user.pk)
    notifications = Notification.objects.all()
    my_class = request.user.my_class
    context = {'notifications': notifications, 'my_class': my_class}
    return render(request, 'notifications_tab.html', context)


def MyTasks(request):

    me = Person.objects.get(id=request.user.pk)
    tasks = TODO.objects.all()
    personal_tasks = TaskCompletion.objects.all()
    my_class = request.user.my_class
    assigned_task = TaskCompletion.objects.filter(user=request.user)
    context = {'tasks': tasks, 'personal_tasks': personal_tasks,
               'me': me, 'my_class': my_class, 'assigned_task': assigned_task}
    return render(request, 'tasks_list.html', context)
