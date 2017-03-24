from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from login.models import PhotoTutorials, PhotoshopBasics, SpecialEffects, LightRoom, TextEffects
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from django import template
import pdb


register = template.Library() 
#def has_group():
#    return user.groups.filter(name='Faculty').exists()
#class Index(forms.ModelForm):
#        """
#        https://docs.djangoproject.com/en/1.9/topics/class-based-views/intro/
#        """
#        template_name = 'login/index.html'
#        password = forms.CharField(widget=forms.PasswordInput)
#        class Meta:
#            model = LoginForm
#       def get(self, request, *args, **kwargs):
#            return render(request, self.template_name,)


def Index(request):
    return render(request, 'login/index.html', {})


def IndexSignUp(request):
    return render(request, 'login/signup.html', {})

def signup(request):
    try:
        if request.method == 'POST':
            usern = request.POST.get('user',None)
            pwd = request.POST.get('pwd',None)
            email = request.POST.get('email',None)
            user = User.objects.create_user(usern, email, pwd)
            user.first_name = request.POST.get('fname', None)
            user.last_name =  request.POST.get('lname',None)
            #user.is_active = False
            user.groups.add(Group.objects.get(name='Students'))
            user.save()
            if(authenticate(username=usern, password=pwd)):
                return render(request, 'login/signup_success.html',)
            else:
                print("ERROR!!!!!!s")
                return render(request, 'login/signup_success.html',)
    except(IntegrityError):
        print("ERROR!!!!!!")
        return render(request, 'login/error_signup.html',)

def signin(request):
    if request.method == 'POST':
        usern = request.POST.get('pupilname', None)
        pwd = request.POST.get('pupilpass', None)
        user = authenticate(username=usern, password=pwd)
        if user is not None:
            print("YAAAAAAY!")
            login(request, user)
            return render(request, 'login/signin_success.html', {'user': user})
        else:
            print("ERROR!!!!")
            return render(request, 'login/error_signin.html')
    else:
        print("ERROR!!!!2")
        return render(request, 'login/error_signin.html')

def log_out(request):
    logout(request)
    #return redirect('../')
    return render(request, 'login/logout.html')


def news(request):
    return render(request, 'login/news.html', {})

def about(request):
    return render(request, 'login/about.html', {})

def IndexSignup_faculty(request):
    return render(request, 'login/IndexSignup_faculty.html', {})

def signup_faculty(request):
    try:
        if request.method == 'POST':
            usern = request.POST.get('user',None)
            pwd = request.POST.get('pwd',None)
            email = request.POST.get('email',None)
            user = User.objects.create_user(usern, email, pwd)
            user.first_name = request.POST.get('fname', None)
            user.last_name =  request.POST.get('lname',None)
            user.is_active = False
            user.groups.add(Group.objects.get(name='Faculty'))
            user.save()
            send_mail(
                'Faculty Register Alert',
                'First Name: ' + user.first_name + 'Last Name: ' + 
                user.last_name + 'Username: ' + usern + 
                'Email Address: ' + email,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=True,
            )
            if(authenticate(username=usern, password=pwd)):
                return render(request, 'login/signup_success_faculty.html',)
            else:
                print("ERROR!!!!!!s")
                return render(request, 'login/signup_success_faculty.html',)
    except(IntegrityError):
        print("ERROR!!!!!!")
        return render(request, 'login/error_signup.html',)


def courses(request):
    faculty = Group.objects.get(name="Faculty")
    x = request.user.groups.all()
    y = None
    if not x:
        return render(request, 'login/courses.html', {'faculty':faculty, 'y':y})
    else:  
        y = x[0]
        return render(request, 'login/courses.html', {'faculty':faculty, 'y':y})

def course1(request):
    faculty = Group.objects.get(name="Faculty")
    if request.user.is_authenticated():
        x = request.user.groups.all()
        y = None
        n = request.user
        if not x:
            try:
                subject = PhotoTutorials.objects.get(students=n)
                return render(request, 'login/course1.html', {'faculty':faculty, 'y':y})
            except:
                return render(request, 'login/course1_register.html', {})
        else:
            try:
                subject = PhotoTutorials.objects.get(students=n)
                return render(request, 'login/course1.html', {'faculty':faculty, 'y':y})
            except:
                y = x[0]
                return render(request, 'login/course1_register.html', {'faculty':faculty, 'y':y})
    else:
        return render(request, 'login/course1_register.html', {})

def register_course1(request):
    faculty = Group.objects.get(name="Faculty")
    if request.user.is_authenticated():
        x = request.user.groups.all()
        y = None
        n = request.user
        if not x:
            try:
                subject = PhotoTutorials(students=n)
                subject.save()
                return render(request, 'login/course1.html', {'faculty':faculty, 'y':y})
            except:
                return render(request, 'login/course1.html', {})
        else:
            subject = PhotoTutorials(students=n)
            subject.save()
            return render(request, 'login/course1.html', {'faculty':faculty, 'y':y})

def course2(request):
    faculty = Group.objects.get(name="Faculty")
    if request.user.is_authenticated():
        x = request.user.groups.all()
        y = None
        n = request.user
        if not x:
            try:
                subject = PhotoshopBasics.objects.get(students=n)
                return render(request, 'login/course2.html', {'faculty':faculty, 'y':y})
            except:
                return render(request, 'login/course2_register.html', {})
        else:
            try:
                subject = PhotoshopBasics.objects.get(students=n)
                return render(request, 'login/course2.html', {'faculty':faculty, 'y':y})
            except:
                y = x[0]
                return render(request, 'login/course2_register.html', {'faculty':faculty, 'y':y})
    else:
        return render(request, 'login/course1_register.html', {})
def register_course2(request):
    faculty = Group.objects.get(name="Faculty")
    if request.user.is_authenticated():
        x = request.user.groups.all()
        y = None
        n = request.user
        if not x:
            try:
                subject = PhotoshopBasics(students=n)
                subject.save()
                return render(request, 'login/course2.html', {'faculty':faculty, 'y':y})
            except:
                return render(request, 'login/course2.html', {})
        else:
            subject = PhotoshopBasics(students=n)
            subject.save()
            return render(request, 'login/course2.html', {'faculty':faculty, 'y':y})

def course3(request):
    faculty = Group.objects.get(name="Faculty")
    if request.user.is_authenticated():
        x = request.user.groups.all()
        y = None
        n = request.user
        if not x:
            try:
                subject = SpecialEffects.objects.get(students=n)
                return render(request, 'login/course3.html', {'faculty':faculty, 'y':y})
            except:
                return render(request, 'login/course3_register.html', {})
        else:
            try:
                subject = SpecialEffects.objects.get(students=n)
                return render(request, 'login/course3.html', {'faculty':faculty, 'y':y})
            except:
                y = x[0]
                return render(request, 'login/course3_register.html', {'faculty':faculty, 'y':y})
    else:
        return render(request, 'login/course1_register.html', {})
def register_course3(request):
    faculty = Group.objects.get(name="Faculty")
    if request.user.is_authenticated():
        x = request.user.groups.all()
        y = None
        n = request.user
        if not x:

            try:
                subject = SpecialEffects(students=n)
                subject.save()
                return render(request, 'login/course3.html', {'faculty':faculty, 'y':y})
            except:
                return render(request, 'login/course3.html', {})
        else:
            subject = SpecialEffects(students=n)
            subject.save()
            return render(request, 'login/course3.html', {'faculty':faculty, 'y':y})

def course4(request):
    faculty = Group.objects.get(name="Faculty")
    if request.user.is_authenticated():
        x = request.user.groups.all()
        y = None
        n = request.user
        if not x:
            try:
                subject = LightRoom.objects.get(students=n)
                return render(request, 'login/course4.html', {'faculty':faculty, 'y':y})
            except:
                return render(request, 'login/course4_register.html', {})
        else:
            try:
                subject = LightRoom.objects.get(students=n)
                return render(request, 'login/course4.html', {'faculty':faculty, 'y':y})
            except:
                y = x[0]
                return render(request, 'login/course4_register.html', {'faculty':faculty, 'y':y})
    else:
        return render(request, 'login/course1_register.html', {})
def register_course4(request):
    faculty = Group.objects.get(name="Faculty")
    if request.user.is_authenticated():
        x = request.user.groups.all()
        y = None
        n = request.user
        if not x:
            try:
                subject = LightRoom(students=n)
                subject.save()
                return render(request, 'login/course4.html', {'faculty':faculty, 'y':y})
            except:
                return render(request, 'login/course4.html', {})
        else:
            subject = LightRoom(students=n)
            subject.save()
            return render(request, 'login/course4.html', {'faculty':faculty, 'y':y})

def course5(request):
    faculty = Group.objects.get(name="Faculty")
    if request.user.is_authenticated():
        x = request.user.groups.all()
        y = None
        n = request.user
        if not x:
            try:
                subject = TextEffects.objects.get(students=n)
                return render(request, 'login/course5.html', {'faculty':faculty, 'y':y})
            except:
                return render(request, 'login/course5_register.html', {})
        else:
            try:
                subject = TextEffects.objects.get(students=n)
                return render(request, 'login/course5.html', {'faculty':faculty, 'y':y})
            except:
                y = x[0]
                return render(request, 'login/course5_register.html', {'faculty':faculty, 'y':y})
    else:
        return render(request, 'login/course1_register.html', {})
def register_course5(request):
    faculty = Group.objects.get(name="Faculty")
    if request.user.is_authenticated():
        x = request.user.groups.all()
        y = None
        n = request.user
        if not x:
            try:
                subject = TextEffects(students=n)
                subject.save()
                return render(request, 'login/course5.html', {'faculty':faculty, 'y':y})
            except:
                return render(request, 'login/course5.html', {})
        else:
            subject = TextEffects(students=n)
            subject.save()
            return render(request, 'login/course5.html', {'faculty':faculty, 'y':y})