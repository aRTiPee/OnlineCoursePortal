from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

#class LoginForm(models.Model):
#    author = models.ForeignKey('auth.User')
#    title = models.CharField(max_length=200)
#    text = models.TextField()
#    created_date = models.DateTimeField(default=timezone.now)
#    published_date = models.DateTimeField(blank=True, null=True)

#    def publish(self):
#       self.published_date = timezone.now()
#        self.save()

#    def __str__(self):
#        return self.title

class SubjectA(models.Model):
    students = models.OneToOneField(User, on_delete=models.CASCADE, 
        primary_key=True, blank=True)

class SubjectB(models.Model):
    students = models.OneToOneField(User, on_delete=models.CASCADE, 
        primary_key=True, blank=True)

class SubjectC(models.Model):
    students = models.OneToOneField(User, on_delete=models.CASCADE, 
        primary_key=True, blank=True)

class SubjectD(models.Model):
    students = models.OneToOneField(User, on_delete=models.CASCADE, 
        primary_key=True, blank=True)

class SubjectE(models.Model):
    students = models.OneToOneField(User, on_delete=models.CASCADE, 
        primary_key=True, blank=True)

