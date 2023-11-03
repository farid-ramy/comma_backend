from django.db import models

# Create your models here.
class products (models.Model):
        name = models.CharField(max_length=50)
        quantity= models.IntegerField()
        price = models.DecimalField(max_digits=7, decimal_places=2)