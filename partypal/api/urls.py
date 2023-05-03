from django.urls import path
from . import views


urlpatterns = [


    path('api', views.apiOverview, name='api-overview'),

    
    # ------------ EVENT -------------
    path('event-list', views.eventList, name='event-list'),
    path('event-detail/<str:pk>/', views.eventDetail, name='event-detail'),
    path('event-create', views.createEvent, name='event-create'),
    path('event-update/<str:pk>/', views.updateEvent, name='event-update'),
    path('event-delete/<str:pk>/', views.deleteEvent, name='event-delete'),
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
