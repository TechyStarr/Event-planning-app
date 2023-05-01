from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Event, Guest, Host, Venue
from .serializers import UserSerializer, EventSerializer, GuestSerializer, HostSerializer, VenueSerializer


@api_view(['GET'])
def home(request):
    routes = [
        'GET/api',
        'GET/api/rooms',
        'GET/api/rooms/:id',
    ]
    return Response(routes) # safe=False allows for lists to be returned


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/event-list/',  
        'Detail View':'/event-detail/<str:pk>/',
        'Create':'/event-create/',
        'Update':'/event-update/<str:pk>/',
        'Delete':'/event-delete/<str:pk>/',
    }
    return Response(api_urls) # safe=False allows for lists to be returned

@api_view(['GET'])
def eventList(request):
    events = Event.objects.all().order_by('-id')
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)
