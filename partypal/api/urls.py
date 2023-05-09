from django.urls import path
from . import views


urlpatterns = [


    path('api', views.apiOverview, name='api-overview'),

    
    # ------------ EVENT -------------
    path('events/', views.listEvent, name='events'),
    path('event/<str:pk>/', views.viewEvent, name='event'),
    path('event-create/', views.createEvent, name='event-create'),
    path('event-update/<str:pk>/', views.updateEvent, name='event-delete'),
    path('event-delete/<str:pk>/', views.deleteEvent, name='event-delete'),

    path('event-search/', views.searchEvent, name='event-search'),
    path('event-register/<str:pk>/', views.registerForEvent, name='event-register'),

]

# {
#     "name": "OscaFest",
#     "description": "An Open Source Community Africa Festival",
#     "Location": "Lagos, Nigeria",
#     "Date": "December 25, 2020",
#     "Time": "12:00 pm",
#     "host": "Open Source Community Africa",
#     "guest": "starr"
# }
