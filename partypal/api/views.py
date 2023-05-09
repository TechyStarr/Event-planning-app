from django.shortcuts import render
from django.db.models import Q
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Event, Venue
from .serializers import EventSerializer
from django.utils import timezone



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

class EventList(APIView):
    @authentication_classes([JWTAuthentication]) 
    @permission_classes([IsAuthenticated])

    def get(self, request, format=None): # format=None allows for multiple data types to be returned
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

    def get(self,  request):
        query = request.GET.get('q') # this line of code is used to get the query from the url 
        if query:
            queryset = Event.objects.filter(
                Q(name__icontains=query) |
                Q(location__icontains=query) |
                Q(description__icontains=query) |
                Q(start_date__icontains=query) 
                # Q(upcoming_events__icontains=query) |
                # Q(past_events__icontains=query) 
                )# filter the queryset based on the query 
            
            serializer = EventSerializer(queryset, many=True) # serialize the queryset 
            return Response(serializer.data)
        else:
            return Response({'events': 'No event found'})
        


class EventDetail(APIView):
    @authentication_classes([JWTAuthentication]) 
    @permission_classes([IsAuthenticated])
    def get_event(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise EventSerializer.NotFound({
                "Event": "This event does not exist"
            })
        
    def get(self, request, pk, format=None):
        event = self.get_event(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        event = self.get_event(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk, format=None):
        event = self.get_event(pk)
        event.delete()
        return Response({
            "Event": "Event successfully deleted"
        })


# class SearchEvent(APIView):
#     @authentication_classes([JWTAuthentication]) 
#     @permission_classes([IsAuthenticated])
#     def get(self, request):
#         query = request.GET.get('q') # this line of code is used to get the query from the url
#         if query:
#             queryset = Event.objects.filter(
#                 Q(name__icontains=query) |
#                 Q(location__icontains=query) |
#                 Q(description__icontains=query) |
#                 Q(start_date__icontains=query) 
#                 # Q(upcoming_events__icontains=query) |
#                 # Q(past_events__icontains=query) 
#                 )# filter the queryset based on the query
#             serializer = EventSerializer(queryset, many=True) # serialize the queryset
#             return Response(serializer.data)
#         else:
#             return Response({'events': 'No event found'})















# ------------- EVENT -----------------












@api_view(['GET'])
def searchEvent(request):
    query = request.GET.get('q') # this line of code is used to get the query from the url 
    if query:
        queryset = Event.objects.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query) |
            Q(description__icontains=query) |
            Q(date__icontains=query) 
            # Q(upcoming_events__icontains=query) |
            # Q(past_events__icontains=query) 
            )# filter the queryset based on the query 
        
        serializer = EventSerializer(queryset, many=True) # serialize the queryset 
        return Response(serializer.data)
    else:
        return Response({'events': 'No event found'})
    

# @api_view(['GET'])
# def recentEvent(request):
#     queryset = Event.objects.all().order_by('-date')[:3]
#     serializer = EventSerializer(queryset, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def upcomingEvent(request):
#     queryset = Event.objects.all().order_by('date')[:3]
#     serializer = EventSerializer(queryset, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def pastEvent(request):
#     queryset = Event.objects.all().order_by('-date')[:3]
#     serializer = EventSerializer(queryset, many=True)
#     return Response(serializer.data)


@api_view(['POST'])
def registerForEvent(request, pk):
    event = Event.objects.get(id=pk) #

    
    event.guests.add(request.user)
    return Response({"success": "You've successfully registered for this event"})

@api_view(['GET'])
def unregisterForEvent(request, pk):
    pass


@api_view(['GET'])
def inviteUser(request, pk):
    pass

@api_view(['GET'])
def uninviteUser(request, pk):
    pass

@api_view(['GET'])
def acceptInvite(request, pk):
    pass

@api_view(['GET'])
def declineInvite(request, pk):
    pass

@api_view(['GET'])
def cancelInvite(request, pk):

    pass

@api_view(['GET'])
def viewHost(request, pk):
    pass

























# @api_view(['GET'])
# def eventByHost(request, pk):
#     queryset = Event.objects.filter(host=pk)
#     serializer = EventSerializer(queryset, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def eventByGuest(request, pk):
#     queryset = Event.objects.filter(guest=pk)
#     serializer = EventSerializer(queryset, many=True)
#     return Response(serializer.data)