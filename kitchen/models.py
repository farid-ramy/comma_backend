from django.db import models

# Create your models here.

class Kitchen(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

