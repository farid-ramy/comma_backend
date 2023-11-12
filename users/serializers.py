from rest_framework import serializers
from users.models import User
from branches.models import Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()

    class Meta:
        model = User
        fields = "__all__"

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



