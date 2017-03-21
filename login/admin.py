from django.contrib import admin
from .models import LoginForm, Student

# Register your models here.



class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'LastName',
        'FirstName',
        'StudentNumber',
        'UserName',
        'BirthDate',
        'Gender',
        'Province_CityAddress',
        'ContactNumber',
        'EmailAddress',
        )

admin.site.register(LoginForm)
admin.site.register(Student, StudentAdmin)
