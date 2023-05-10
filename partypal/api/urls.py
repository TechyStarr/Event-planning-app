from django.urls import path
from . import views


urlpatterns = [


    path('api', views.apiOverview, name='api-overview'),

    
    # ------------ EVENT -------------
    path('events/', views.EventList.as_view(), name='events'),
    path('event/<int:pk>/', views.EventDetail.as_view(), name='event'),
    path('event-search/', views.SearchEvent.as_view(), name='event-search'),
    path('event-register/<int:pk>/', views.RegisterForEvent.as_view(), name='event-register'),
    path('event/<int:event_id>/user/<int:user_id>/', views.GuestInvite.as_view(), name='event-invite')
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
