from rest_framework import serializers
from .models import Package
from branches.models import Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()

    class Meta:
        model = Package
        fields = "__all__"

class CreatePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"



