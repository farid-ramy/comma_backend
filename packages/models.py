from django.db import models
    
class Package (models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name




