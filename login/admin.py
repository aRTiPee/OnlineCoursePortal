from django.contrib import admin
from login.models import SubjectA, SubjectB, SubjectC, SubjectD, SubjectE
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

class Subject_Student_Display(admin.ModelAdmin):
    list_display = (
        'students',
        )
    
admin.site.register(SubjectA, Subject_Student_Display)
admin.site.register(SubjectB, Subject_Student_Display)
admin.site.register(SubjectC, Subject_Student_Display)
admin.site.register(SubjectD, Subject_Student_Display)
admin.site.register(SubjectE, Subject_Student_Display)