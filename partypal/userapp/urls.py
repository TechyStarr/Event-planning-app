from django.urls import path
from . import views
from .serializer import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)





urlpatterns = [

    # ------------ AUTHENTICATION WITH SIMPLE JWT -------------
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    # ------------ USER -------------
    path('users/', views.UserList.as_view(), name='users'),
    path('user/<str:pk>/', views.UserDetail.as_view(), name='user'),
]
