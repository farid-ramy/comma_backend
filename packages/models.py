from django.db import models
    
class Package (models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name




