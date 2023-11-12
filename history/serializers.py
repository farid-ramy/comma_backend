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
    client_id = serializers.SerializerMethodField()
    employee_id = serializers.SerializerMethodField()
    branch_id = serializers.SerializerMethodField()

    class Meta:
        model = History
        fields = "__all__"

    def get_client_id(self, obj):
        client = User.objects.filter(branch=obj)
        return UserSerializer(client, many=True).data

    def get_employee_id(self, obj):
        client = User.objects.filter(branch=obj)
        return UserSerializer(client, many=True).data

    def get_branch_id(self, obj):
        branch = Branch.objects.filter(branch=obj)
        return BranchSerializer(branch, many=True).data
