from django.contrib import admin
from login.models import PhotoTutorials, PhotoshopBasics, SpecialEffects, LightRoom, TextEffects
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

class Label(admin.ModelAdmin):
    list_display = (
        'students',
        )
    
admin.site.register(PhotoTutorials, Label)
admin.site.register(PhotoshopBasics, Label)
admin.site.register(SpecialEffects, Label)
admin.site.register(LightRoom, Label)
admin.site.register(TextEffects, Label)