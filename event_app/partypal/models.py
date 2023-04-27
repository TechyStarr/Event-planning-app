from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    attendees = models.ManyToManyField('Attendee', blank=True, related_name='events')

    def __str__(self):
        return self.title