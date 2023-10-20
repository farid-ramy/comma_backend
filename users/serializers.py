from rest_framework.serializer import Modelserializer
from .models import User


class UserSerializer(Modelserializer):
    class Meta:
        model = User
        fields = '__all__'