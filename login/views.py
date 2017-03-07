from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib import auth
from django import forms
from login.models import *

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

class Faculty(View):
        """
        https://docs.djangoproject.com/en/1.9/topics/class-based-views/intro/
        """
        template_name = 'login/faculty.html'

        def get(self, request, *args, **kwargs):
            return render(request, self.template_name,)

        def post(self, request, *args, **kwargs):
            pass
