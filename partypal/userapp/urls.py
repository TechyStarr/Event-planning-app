from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)





urlpatterns = [

    # ------------ AUTHENTICATION WITH SIMPLE JWT -------------
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ------------ USER -------------
    path('user-list', views.userList, name='user-list'),
    path('user-detail/<str:pk>/', views.userDetail, name='user-detail'),
    path('user-create', views.createUser, name='user-create'),
    path('user-update', views.updateUser, name='user-update'),
    path('user-delete/<str:pk>/', views.deleteUser, name='user-delete'),
]
