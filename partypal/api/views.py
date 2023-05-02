from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Event, Guest, Host, Venue
from .serializers import UserSerializer, EventSerializer, GuestSerializer, HostSerializer, VenueSerializer

@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializers = UserSerializer(users, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def createUser(request):
    users = User.objects.all()
    serializers = UserSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


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
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def eventDetail(request, pk):
    events = Event.objects.get(id=pk)
    serializer = EventSerializer(events, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createEvent(request):
    events = Event.objects.all()
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['PUT'])
def updateEvent(request, pk):
    events = Event.objects.get(id=pk)
    serializer = EventSerializer(instance=events, data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)