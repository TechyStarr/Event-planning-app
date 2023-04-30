from rest_framework import serializers
from .models import User, Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'name', 'email', 'password']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['pk', 'name', 'description', 'date', 'location', 'host', 'guests']
