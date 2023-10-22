from django.db import models

# Create your models here.
class Branches(models.Model):
  name = models.CharField(max_length=255)
  adress = models.TextField(blank=True, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)

    
  def __str__(self):
    return self.name