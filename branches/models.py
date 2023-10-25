from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    manager_name = models.CharField(max_length=50, blank=True)
    opening_hours = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name
    
    def get_kitchen(self):
        from .models import kitchen  # Import Kitchen lazily
        try:
            return self.kitchen
        except kitchen.DoesNotExist:
            return None
