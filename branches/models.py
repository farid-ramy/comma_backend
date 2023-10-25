from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    manager_name = models.CharField(max_length=50, null=True, blank=True)
    opening_hours = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return self.name