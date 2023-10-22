from django.db import models

# # Create your models here.
# class Branch(models.Model):
#     name = models.CharField(max_length=100)
    
class Package (models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='packages')
    def __str__(self):
        return self.name



# Create your models here.
