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
    

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.event} - {self.quantity} - {self.total}'
    
    # def save(self, *args, **kwargs):

    #     self.total = self.quantity * self.price
    #     super().save(*args, **kwargs)


class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendees')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='attendees')
    purchase_date = models.BooleanField(default=False)
    # checked_in_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.event} - {self.checked_in}'


class Organizer(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='organizers')
    email_address = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizers')
    

class Venue(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='venue')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='venue')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='venue')
    purchase_date = models.BooleanField(default=False)
    # checked_in_on = models.DateTimeField(auto_now_add=True)


