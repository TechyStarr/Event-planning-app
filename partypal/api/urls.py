from django.urls import path
from . import views


urlpatterns = [


    path('api', views.apiOverview, name='api-overview'),

    
    # ------------ EVENT -------------
    path('events/', views.EventList.as_view(), name='events'),
    path('event/<int:pk>/', views.EventDetail.as_view(), name='event'),
    path('event/', views.SearchEvent.as_view(), name='event-search'),
    path('event/register/<int:pk>/', views.RegisterForEvent.as_view(), name='event-register'),
    path('event/invite/<int:event_id>/user/<int:user_id>/', views.GuestInvite.as_view(), name='event-invite'),
    path('event/remove/<int:event_id>/user/<int:user_id>/', views.RemoveGuest.as_view(), name='event-remove-guest'),
    path('event/guestlist/<int:event_id>/', views.RetrieveEventGuestList.as_view(), name='event-guestlist'),
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
