from django.db import models


from django.db import models
from branches.models import Branch  

class Room(models.Model):
    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=20, choices=[('shared', 'Shared Room'), ('quiet', 'Quiet Room'), ('meeting', 'Meeting Room')])
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='roomssBranch_id', default=None)

class MeetingReservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

