from rest_framework.serializers import ModelSerializer
from .models import Branch,WorkingIN

class BranchSerializer(ModelSerializer):
  class Meta:
    model = Branch 
    fields = "__all__"

class WorkingINSerializer(ModelSerializer):
  class Meta:
    model = WorkingIN 
    fields = "__all__"