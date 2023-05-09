from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User, Event, Venue
from django.utils import timezone


class VenueSerializer(ModelSerializer):
    class Meta:
        model = Venue
        fields = "__all__"


class EventSerializer(ModelSerializer):
    venue = serializers.PrimaryKeyRelatedField(queryset=Venue.objects.all())
    custom_venue = VenueSerializer(required=False)

    class Meta:
        model = Event
        fields = "__all__" # fields to be serialized
        
        # def validate(self, data):
        #     """
        #     Check that the start is before the stop.
        #     """
        #     if data['start_date'] > data['end_date']:
        #         raise serializers.ValidationError("finish must occur after start")
        #     return data
        
    def validate(self, data):
        super().validate(data) # call the default validate method first to ensure all fields are valid

        if data['venue'].id == 2 and not data.get('custom_venue'):
            raise serializers.ValidationError({"custom_venue": "Custom must be provided if venue is Other"})
        
        return data
    
    def create(self, validated_data):
        venue = validated_data.pop('venue')

        if validated_data.get('custom_venue'):
            venue = Venue.objects.create(**validated_data.pop('custom_venue'))
    
        event = Event.objects.create(venue=venue, **validated_data)
        return event


class SearchEventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id', 
            'name', 
            'start_date', 
            'location',
            'description', 
            'created_at'
            )


class registerForEventSerializer(ModelSerializer):
    event_id = serializers.IntegerField()






# class HostSerializer(ModelSerializer):
#     class Meta:
#         model = Host
#         fields = ('id', 'name', 'email', 'phone', 'event')



