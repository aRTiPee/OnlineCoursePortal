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

#class Subject(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, blank=True)
#    subjectA = models.CharField(max_length=500, blank=True)
#    subjectB = models.CharField(max_length=500, blank=True)
#    subjectC = models.CharField(max_length=500, blank=True)
#    subjectD = models.CharField(max_length=500, blank=True)
#    subjectE = models.CharField(max_length=500, blank=True)


