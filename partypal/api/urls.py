from django.urls import path
from . import views


urlpatterns = [


    path('api', views.apiOverview, name='api-overview'),

    
    # ------------ EVENT -------------
    path('list-event/', views.listEvent, name='list-event'),
    path('view-event/<str:pk>/', views.viewEvent, name='view-event'),
    path('create-event/', views.createEvent, name='create-event'),
    path('update-event/<str:pk>/', views.updateEvent, name='update-event'),
    path('delete-event/<str:pk>/', views.deleteEvent, name='delete-event'),
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
