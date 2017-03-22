from django.shortcuts import render, redirect, get_object_or_404
from .models import LoginForm, Student
from .forms import StudentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError

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

def Index2(request):
    return render(request, 'login/full-width.html', {})

def Index3(request):
    return render(request, 'login/style-demo.html', {})

def Index4(request):
    return render(request, 'login/signup.html', {})

def signup(request):
    if request.method == 'POST':
        try:
            usern = request.POST.get('user',None)
            pwd = request.POST.get('pwd',None)
            email = request.POST.get('email',None)
            user = User.objects.create_user(usern, email, pwd)
            user.first_name = request.POST.get('fname', None)
            user.last_name =  request.POST.get('lname',None)
            user.save()
            if(authenticate(username=usern, password=pwd)):
                return render(request, 'login/index.html',)
        except(IntegrityError):
            print("ERROR!!!!!!")
            return render(request, 'login/index.html',)

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