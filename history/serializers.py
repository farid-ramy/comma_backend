from rest_framework import serializers
from .models import History
from users.models import User
from branches.models import Branch

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"

class CreateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"

class HistorySerializer(serializers.ModelSerializer):
    client = UserSerializer()
    employee = UserSerializer()
    branch = BranchSerializer()

    class Meta:
        model = History
        fields = "__all__"
