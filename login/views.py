from django.shortcuts import render, redirect, get_object_or_404
#from .models import Subjects
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from django import template

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

def courses(request):
    faculty = Group.objects.get(name="Faculty")
    x = request.user.groups.all()
    y = None
    if not x:
        return render(request, 'login/courses.html', {'faculty':faculty, 'y':y})
    else:  
        y = x[0]
        return render(request, 'login/courses.html', {'faculty':faculty, 'y':y})

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
            if(authenticate(username=usern, password=pwd)):
                return render(request, 'login/signup_success_faculty.html',)
            else:
                print("ERROR!!!!!!s")
                return render(request, 'login/signup_success_faculty.html',)
    except(IntegrityError):
        print("ERROR!!!!!!")
        return render(request, 'login/error_signup.html',)




#class Faculty(View):
#        """
#        https://docs.djangoproject.com/en/1.9/topics/class-based-views/intro/
#        """
#        template_name = 'login/faculty.html'
#
#        def get(self, request, *args, **kwargs):
#            return render(request, self.template_name,)
#
#        def post(self, request, *args, **kwargs):
#            pass
'''
u.Student.BirthDate = request.POST.get('bday',None)
u.Student.StreetAddress = request.POST.get('sadd',None)
            u.Student.MunicipalityAddress = request.POST.get('madd',None)
            u.Student.Province_CityAddress = request.POST.get('padd',None)
            u.Student.ZIPCode = request.POST.get('zip',None)
            u.Student.ContactNumber = request.POST.get('mob',None)
'''