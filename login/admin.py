from django.contrib import admin
#from .models import Subject
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

#class Subject_Student_Display(admin.ModelAdmin):
#    list_display = (
#        'user',
#        'subjectA',
#        'subjectB',
#        'subjectC',
#        'subjectD',
#        'subject',
#    )

#admin.site.register(Subject, Subject_Student_Display)