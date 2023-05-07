from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User, Event, Venue
from django.utils import timezone



class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'location', 'description', 'created_at')


class SearchEventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'location', 'description', 'created_at')


class registerForEventSerializer(ModelSerializer):
    event_id = serializers.IntegerField()
    





# class HostSerializer(ModelSerializer):
#     class Meta:
#         model = Host
#         fields = ('id', 'name', 'email', 'phone', 'event')

# class VenueSerializer(ModelSerializer):
#     class Meta:
#         model = Venue
#         fields = ('id', 'name', 'address', 'event')

# Path: partypal\api\views.py