from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer, UserSerializer

# Create your views here.


@api_view(['GET'])
def home(request):
    routes = [
        'GET/api',
        'GET/api/rooms',
        'GET/api/rooms/:id',
    ]
    return Response(routes)

class EventViewset(viewsets.ModelViewSet):
    query_set = Event.objects.all()
    serializer_class  = EventSerializer
