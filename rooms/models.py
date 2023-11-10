from django.db import models
from branches.models import Branch

# Create your models here.
class Room(models.Model):
    quiet_area = models.PositiveIntegerField(default=0)
    shared_area = models.PositiveIntegerField(default=0)
    meeting_rooms = models.PositiveIntegerField(default=0)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='roomsBranch_id', default=None)
