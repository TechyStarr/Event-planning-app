from django.urls import path
from . import views


urlpatterns = [
    path('api', views.apiOverview, name='api-overview'),
    path('event-list', views.eventList, name='event-list')
]

