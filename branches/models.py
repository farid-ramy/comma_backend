from django.db import models
from users.models import User

class Branch(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField(blank=True ,null=True)
    phone = models.CharField(max_length=15, blank=True,null=True)
    opening_hours = models.CharField(max_length=100, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 
    working_employees = models.ManyToManyField(User, related_name='working_employees', blank=True)

    def __str__(self):
        return self.name
