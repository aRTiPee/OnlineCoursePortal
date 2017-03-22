from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class LoginForm(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    StudentNumber = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100, blank=True)
    LastName = models.CharField(max_length=100, blank=True)
    BirthDate = models.DateField(null=True, blank=True)
    Gender = models.CharField(max_length=1, blank=True)
    UserName = models.CharField(max_length=100, blank=True)
    Password = models.CharField(max_length=100, blank=True)
    StreetAddress = models.CharField(max_length=100, blank=True)
    MunicipalityAddress = models.CharField(max_length=100, blank=True)
    Province_CityAddress = models.CharField(max_length=100, blank=True)
    ZIPCode = models.IntegerField(null=True, blank=True)
    ContactNumber = models.IntegerField(null=True, blank=True)
    EmailAddress = models.EmailField(null=True, blank=True)

    def publish(self):
        self.save()

