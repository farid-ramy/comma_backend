from django.db import models

# Create your models here.

class Kitchen(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # branch = models.OneToOneField('yourapp.Branch', on_delete=models.CASCADE)
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()