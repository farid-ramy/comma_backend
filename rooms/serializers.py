from rest_framework import serializers
from .models import Room, Reservation
from users.models import User
from branches.models import Branch

class BranchSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Branch
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = "__all__"

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()  

    class Meta:
        model = Room
        fields = "__all__"

class CreateReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    room = CreateRoomSerializer()  
    client = UserSerializer()  

    class Meta:
        model = Reservation
        fields = "__all__"


from django.db import models

from rest_framework import serializers
from .models import Room, Reservation
from users.models import User
from branches.models import Branch

class BranchSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Branch
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = "__all__"

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()  

    class Meta:
        model = Room
        fields = "__all__"

class CreateReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    room = CreateRoomSerializer()  
    client = UserSerializer()  

    class Meta:
        model = Reservation
        fields = "__all__"


