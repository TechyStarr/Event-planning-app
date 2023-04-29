from rest_framework.serializers import ModelSerializer
from .models import User, Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'name', 'email', 'password']
