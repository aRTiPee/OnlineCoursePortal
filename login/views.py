from django.shortcuts import render, redirect, get_object_or_404
from .models import LoginForm, Student
from .forms import StudentForm
from django.contrib.auth import authenticate, login, logout

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
        stu = StudentForm(request.POST)
        if stu.is_valid():
            stud = stu.save(commit=False)
            stud.FirstName = request.POST.get('fname', None)
            stud.LastName = request.POST.get('lname',None)
            stud.BirthDate = request.POST.get('bday',None)
            stud.Gender = request.POST.get('gen',None)
            stud.UserName = request.POST.get('user',None)
            stud.Password = request.POST.get('pwd',None)
            stud.StreetAddress = request.POST.get('sadd',None)
            stud.MunicipalityAddress = request.POST.get('madd',None)
            stud.Province_CityAddress = request.POST.get('padd',None)
            stud.ZIPCode = request.POST.get('zip',None)
            stud.ContactNumber = request.POST.get('mob',None)
            stud.EmailAddress = request.POST.get('email',None)
            stud.save()
            return redirect('../')

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
