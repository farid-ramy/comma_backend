from .models import products
from rest_framework import serializers
from branches.models import Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()

    class Meta:
        model = products
        fields = "__all__"


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = "__all__"

   