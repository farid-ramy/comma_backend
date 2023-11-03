from rest_framework import serializers
from .models import Kitchen
from .models import Branch
from .models import Product

class KitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen
        fields = '__all__'
