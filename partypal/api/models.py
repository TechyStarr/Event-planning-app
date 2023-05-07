from typing import Any
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from userapp.models import User
from PIL import Image
from django.utils import timezone
from datetime import datetime


# Create your models here.



class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField(default=datetime(2023, 6, 10, 10, 30))
    end_date = models.DateTimeField(default=datetime(2023, 6, 10, 12, 0))
    location = models.CharField(max_length=100)
    host = models.ForeignKey(User, related_name='events_hosted', default="", null=True, blank=True, on_delete=models.CASCADE)
    guests = models.ManyToManyField(User, related_name='registered_guests', blank=True, default=[])
    capacity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='event_images/', blank=True)
    venue = models.ForeignKey('Venue', related_name='events', default="", blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    

class Host(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hosts', default="Amaino")
    bio = models.TextField(max_length=100, default="")
    events_hosted = models.ManyToManyField(Event, related_name='hosts', blank=True, default=[])
    events_hosting = models.ManyToManyField(Event, related_name='hosted_events', blank=True, default=[])
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0) # max_digits is the total number of digits allowed, decimal_places is the number of digits allowed after the decimal point

    def __str__(self):
        return self.name

    

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    capacity = models.IntegerField(default=0)
    contact_name = models.CharField(max_length=100, default="")
    contact_email = models.EmailField(max_length=100, default="")
    contact_phone = models.CharField(max_length=100, default="")
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0) # max_digits is the total number of digits allowed, decimal_places is the number of digits allowed after the decimal point
    event = models.ForeignKey(Event, related_name='venues', default="", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
