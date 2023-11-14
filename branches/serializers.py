from rest_framework import serializers
from .models import Branch
from users.models import User
from packages.models import Package
from rooms.models import Room,Reservation

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

class BranchSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    packages = serializers.SerializerMethodField()
    rooms = serializers.SerializerMethodField()
    reservations = serializers.SerializerMethodField()

    class Meta:
        model = Branch
        fields = "__all__"
      
    def get_users(self, obj):
      users = User.objects.filter(branch=obj)
      return UserSerializer(users, many=True).data
    
    def get_packages(self, obj):
      packages = Package.objects.filter(branch=obj)
      return PackageSerializer(packages, many=True).data
    
    def get_rooms(self, obj):
      rooms = Room.objects.filter(branch=obj)
      return RoomSerializer(rooms, many=True).data
    
    def get_reservations(self, obj):
        rooms = Room.objects.filter(branch=obj)
        reservations = Reservation.objects.filter(room__in=rooms)

        return ReservationSerializer(reservations, many=True).data

class CreateBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"
