from django.shortcuts import render
from django.db.models import Q
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Event, Venue, Host
from .serializers import EventSerializer, HostSerializer, VenueSerializer
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

# tested
class EventList(APIView):
    @authentication_classes([JWTAuthentication]) 
    @permission_classes([IsAuthenticated])

    def get(self, request, format=None): # format=None allows for multiple data types to be returned
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    # needs to bw fixed
    def post(self, request, format=None):
        event_serializer = EventSerializer(data=request.data)
        if event_serializer.is_valid():
            
            user = request.user
            event_serializer.save(host=user)

            # create and save host object
            host = Host(user=user)
            host.save()

            return Response(event_serializer.data)
        return Response(event_serializer.errors)



# tested
class EventDetail(APIView):
    @authentication_classes([JWTAuthentication]) 
    @permission_classes([IsAuthenticated])
    def get_event(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise EventSerializer.NotFound({
                "Event": "This event was not found"
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


# tested
class SearchEvent(APIView):
    @authentication_classes([JWTAuthentication]) 
    @permission_classes([IsAuthenticated])
    def get(self, request):
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



# tested
class RegisterForEvent(APIView):
    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])

    def post(self, request, pk, format=None): # format=None allows for multiple data types to be returned
        event = Event.objects.get(id=pk) # get the event with the id
        if event:
            user = User.objects.get(id=request.user.id) # get the user with the id
            if user in event.guests.all(): # check if the user is already registered for the event
                return Response({"error": "You're already registered for this event"})
            event.guests.add(user) # add the user to the event
            return Response({"success": "You've successfully registered for this event"})
        else:
            return Response({"error": "Event not found"})
        




# tested
class GuestInvite(APIView):
    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])

    def post(self, request, user_id, event_id):
        event = Event.objects.get(id=event_id)
        if event:
            user = User.objects.get(id=user_id)
            if user:
                event.guests.add(user)
                event.save()
                return Response({"success": f"You just invited {user} to this event"})
            return Response({"User": "User does not exist"})
        else:
            return Response({"error": "Event not found"})


# tested
class RemoveGuest(APIView):
    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])
    def post(self, request, user_id, event_id):
        event = Event.objects.get(id=event_id)
        if event:
            user = User.objects.get(id=user_id)
            if user:
                event.guests.remove(user)
                event.save()
                serializer = EventSerializer(event)
                guest_list = serializer.data.get("guests")
                response_data = {
                "Message": f"You've removed {user} from this event",
                "Updated guest_list": guest_list,
                }
                return Response(response_data)
            return Response({"User": "User does not exist"})
        else:
            return Response({"error": "Event not found"})
        






# tested
class RetrieveEventGuestList(APIView):
    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])
    def get(self, request, event_id):
        event = Event.objects.get(id=event_id)
        if event:
            serializer = EventSerializer(event)
            guest_list = serializer.data.get("guests")
            response_data = {
                "Message": f"Attached below is the guest list for {event.name}",
                "Guests": guest_list,
            }
            return Response(response_data)
        else:
            return Response({"error": "Event not found"})




# test this
class ViewHost(APIView):
    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])

    def get(self, request, event_id):
        event = Event.objects.get(id=event_id)
        if event:
            host = event.host
            serializer = HostSerializer(host)
            return Response(serializer.data)
        else:
            return Response({"error": "Event not found"})















# ------------- EVENT -----------------






@api_view(['GET'])
def recentEvent(request):
    queryset = Event.objects.all().order_by('-date')[:3]
    serializer = EventSerializer(queryset, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
def upcomingEvent(request):
    queryset = Event.objects.all().order_by('date')[:3]
    serializer = EventSerializer(queryset, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def pastEvent(request):
#     queryset = Event.objects.all().order_by('-date')[:3]
#     serializer = EventSerializer(queryset, many=True)
#     return Response(serializer.data)



@api_view(['GET'])
def unregisterForEvent(request, pk):
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