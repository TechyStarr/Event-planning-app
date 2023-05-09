from django.urls import path
from . import views


urlpatterns = [


    path('api', views.apiOverview, name='api-overview'),

    
    # ------------ EVENT -------------
    path('events/', views.EventList.as_view(), name='events'),
    path('event/<int:pk>/', views.EventDetail.as_view(), name='event'),
    path('event-search/', views.SearchEvent.as_view(), name='event-search'),

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
