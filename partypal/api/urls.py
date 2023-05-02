from django.urls import path
from . import views


urlpatterns = [


    path('api', views.apiOverview, name='api-overview'),

    # ------------ USER -------------
    path('user-list', views.userList, name='user-list'),
    path('user-detail/<str:pk>/', views.userDetail, name='user-detail'),
    path('user-create', views.createUser, name='user-create'),
    path('user-update', views.updateUser, name='user-update'),

    # ------------ EVENT -------------
    path('event-list', views.eventList, name='event-list'),
    path('event-detail/<str:pk>/', views.eventDetail, name='event-detail'),
    path('event-create', views.createEvent, name='event-create'),
    path('event-update/<str:pk>/', views.updateEvent, name='event-update'),
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
