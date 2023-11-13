from rest_framework import serializers
from .models import Product
from branches.models import Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
  branch = BranchSerializer()

  class Meta:
    model = Product
    fields = "__all__"

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"