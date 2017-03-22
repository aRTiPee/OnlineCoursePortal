from django import forms

from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('FirstName', 'LastName', 'BirthDate', 'Gender', 'UserName', 'Password', 'StreetAddress', 'MunicipalityAddress', 
            'Province_CityAddress', 'ZIPCode', 'ContactNumber', 'EmailAddress')