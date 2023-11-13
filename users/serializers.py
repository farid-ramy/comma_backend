from rest_framework import serializers
from users.models import User
from branches.models import Branch
from history.models import History

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()
    # history = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = "__all__"

    # def get_history(self, obj):
    #     Histories = History.objects.filter(history=obj)
    #     return HistorySerializer(Histories, many=True).data

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



