from django import forms

from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('FirstName', 'LastName', 'UserName', 'Password', 'EmailAddress', 'BirthDate', 'Gender', 'StreetAddress', 'MunicipalityAddress', 
            'Province_CityAddress', 'ZIPCode', 'ContactNumber')