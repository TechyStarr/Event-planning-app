from typing import Any
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


# Create your models here.

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password, **extra_fields):
#         if not username:
#             raise ValueError('The username must be set')
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_superuser(self, username, password, **extra_fields):
#         extra_fields.setdefault('is_organizer', True)
#         extra_fields.setdefault('is_guest', True)
#         extra_fields.setdefault('super_user', True)
#         return self.create_user(username, password, **extra_fields)
    




class User(AbstractUser):
    is_organizer = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    host = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    guests = models.ManyToManyField(User, related_name='guests')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Host(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    event = models.ForeignKey(Event, related_name="hosts", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
