from rest_framework.serializers import ModelSerializer # ModelSerializer is a class that will automatically create a serializer with fields that correspond to the Model fields.
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers # serializers is a module that will allow us to create a serializer manually.




# --------------- TOKEN GENERATION  -----------

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user) # super() calls the parent class's get_token() method and returns the token that was generated for the user.

        # Add custom claims
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



# --------------- USER SERIALIZER -----------------
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_active','is_superuser', 'date_joined', 'last_login'
                )
                

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) # **validated_data passes in the validated data as keyword arguments
        return user

class TokenPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs) # super() calls the parent class's validate() method and returns the data dictionary that was returned by that method. 
        refresh = self.get_token(self.user)
        data['refresh_token'] = str(refresh)
        data['access_token'] = str(refresh.access_token) # refresh.access_token is the access token that was generated for the user.
        return data

