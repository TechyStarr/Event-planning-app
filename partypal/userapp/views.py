from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['GET'])
def apiOverview(request):
    """
    List all code snippets, or create a new snippet.
    """
    api_urls = {
        'List':'/user-list/',  
        'Detail View':'/user-detail/<str:pk>/',
        'Create':'/user-create/',
        'Update':'/user-update/<str:pk>/',
        'Delete':'/user-delete/<str:pk>/',
    }
    return Response(api_urls) # safe=False allows for lists to be returned




class UserList(APIView):
    @authentication_classes([JWTAuthentication]) # 
    @permission_classes([IsAuthenticated])

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    




class UserDetail(APIView):
    @authentication_classes([JWTAuthentication]) # 
    @permission_classes([IsAuthenticated])

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise UserSerializer.NotFound({
                "User": "This user does not exist"
            })
        
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response({
            "User": "User successfully deleted"
        })






class SearchUser(APIView):

    def get(self,  request):
        query = request.GET.get('q') # this line of code is used to get the query from the url 
        if query:
            queryset = User.objects.filter(
                Q(username__icontains=query) 
            )
            serializer = UserSerializer(queryset, many=True) # serialize the queryset 
            return Response(serializer.data)
        else:
            return Response({'Users': 'No user found'})
        












# ------------- USER -----------------


