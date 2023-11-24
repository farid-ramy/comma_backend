from django.db import models
from branches.models import Branch  
from users.models import User

class Room(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch , on_delete=models.CASCADE, related_name='roomsbranch_id', default=None)

    def __str__(self) :
        return f"{self.name} {self.branch.name}"
    
class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    client= models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_id', default=None)
    start_time = models.DateTimeField(default=None,null = True,blank= True)
    end_time = models.DateTimeField(default=None,null= True,blank= True)

    def __str__(self) :
        return f"{self.room.name} {self.client.first_name} {self.start_time}"
    
