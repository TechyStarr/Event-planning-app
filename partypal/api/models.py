from typing import Any
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from userapp.models import User


# Create your models here.



class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()
    # host = models.ForeignKey(User, related_name='events', blank=True, on_delete=models.CASCADE)
    guests = models.ManyToManyField(User, related_name='guests', blank=True)
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
    
