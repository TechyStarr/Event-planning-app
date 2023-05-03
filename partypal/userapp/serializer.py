from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_active','is_superuser', 'date_joined', 'last_login'
                )
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }


