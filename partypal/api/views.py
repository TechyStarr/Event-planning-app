from django.shortcuts import render
from django.db.models import Q
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Event, Guest, Host, Venue
from .serializers import EventSerializer

# Create your views here.




@api_view(['GET'])
def apiOverview(request):
    """
    List all code snippets, or create a new snippet.
    """
    api_urls = {
        'List':'/event-list/',  
        'Detail View':'/event-detail/<str:pk>/',
        'Create':'/event-create/',
        'Update':'/event-update/<str:pk>/',
        'Delete':'/event-delete/<str:pk>/',
    }
    return Response(api_urls) # safe=False allows for lists to be returned






# ------------- EVENT -----------------
@api_view(['GET'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def listEvent(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def viewEvent(request, pk):
    events = Event.objects.get(id=pk)
    serializer = EventSerializer(events, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def createEvent(request):
    events = Event.objects.all()
    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def updateEvent(request, pk):
    events = Event.objects.get(id=pk)
    serializer = EventSerializer(instance=events, data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return Response('Item successfully deleted')


@api_view(['GET'])
def searchEvent(request):
    query = request.GET.get('q') # this line of code is used to get the query from the url 
    if query:
        queryset = Event.objects.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query) |
            Q(description__icontains=query)
            )# filter the queryset based on the query 
        
        serializer = EventSerializer(queryset, many=True) # serialize the queryset 
        return Response(serializer.data)
    else:
        return Response({'events': 'No event found'})
    

    serializer = EventSerializer(data=request.data) 
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'location', 'description']



    def get_queryset(self):
        queryset = Event.objects.all() 
        return queryset