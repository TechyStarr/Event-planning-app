from typing import Any
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from userapp.models import User
from PIL import Image
from django.utils import timezone


# Create your models here.



class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    host = models.ForeignKey(User, related_name='events', default="", blank=True, on_delete=models.CASCADE)
    guests = models.ManyToManyField(User, related_name='guests', blank=True, default=[])
    capacity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='event_images/', blank=True)
    venue = models.ForeignKey('Venue', related_name='events', default="", blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(self, Event).save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    

class Host(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1) # max_digits is the total number of digits allowed, decimal_places is the number of digits allowed after the decimal point

    def __str__(self):
        return self.name
    
class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100)

    def __str__(self):
        return self.user.username
    

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    capacity = models.IntegerField()
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1) # max_digits is the total number of digits allowed, decimal_places is the number of digits allowed after the decimal point
    event = models.ForeignKey(Event, related_name='venues', default="", blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
