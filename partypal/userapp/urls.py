from django.urls import path
from . import views




urlpatterns = [


    # ------------ USER -------------
    path('user-list', views.userList, name='user-list'),
    path('user-detail/<str:pk>/', views.userDetail, name='user-detail'),
    path('user-create', views.createUser, name='user-create'),
    path('user-update', views.updateUser, name='user-update'),
    path('user-delete/<str:pk>/', views.deleteUser, name='user-delete'),


]
