from django.db import models
from django.utils import timezone
import re
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class LoginForm(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)