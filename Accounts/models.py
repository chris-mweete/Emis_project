from django.db import models
from django.contrib.auth.models import User
 

# Create your models here.

class Institution(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    acronym = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    Insititution = models.ForeignKey (Institution, related_name= 'Profile', null=True, blank=True, on_delete= models.SET_NULL)
    user = models.OneToOneField(User, related_name= 'Profile', null=True, blank=True, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
