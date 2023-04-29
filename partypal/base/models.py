from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    password = models.IntegerField()
    # events = models.ManyToManyField(Event, related_name='events,', blank=True)



class Event(models.Model):
    # image = models.ImageField()
    event_name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True) #
    event_date = models.DateField()
    # attendants = models.ManyToManyField(User, related_name='attendants,', blank=True)
    event_time = models.TimeField()
    posted_on = models.DateTimeField(auto_now_add=True) # auto_now_add means that the date and time will be added automatically when the object is created


    def __str__(self):
        return self.event_name
    


