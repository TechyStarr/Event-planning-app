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
    path('user-list/', views.userList, name='user-list'),
    path('view-user/<str:pk>/', views.viewUser, name='view-user'),
    path('register/', views.register, name='register'),
    path('update-user/<str:pk>/', views.updateUser, name='update-user'),
    path('delete-user/<str:pk>/', views.deleteUser, name='delete-user'),



    # path('login/', views.login, name='login'),
]
