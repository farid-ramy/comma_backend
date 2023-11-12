from rest_framework import serializers
from .models import Branch
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class BranchSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    class Meta:
        model = Branch
        fields = "__all__"
      
    def get_users(self, obj):
      users = User.objects.filter(branch=obj)
      return UserSerializer(users, many=True).data

class CreateBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"
