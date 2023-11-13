# serializers.py in the rooms app
from rest_framework import serializers
from .models import Room, MeetingReservation
from branches.serializers import BranchSerializer  # Import the BranchSerializer

class RoomSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()  

    class Meta:
        model = Room
        fields = ['id', 'name', 'room_type', 'branch']

class MeetingReservationSerializer(serializers.ModelSerializer):
    room = RoomSerializer()  

    class Meta:
        model = MeetingReservation
        fields = ['id', 'room', 'start_time', 'end_time', 'purpose']
