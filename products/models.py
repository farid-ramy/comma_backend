from django.db import models
from branches.models import Branch

class Product (models.Model):
        name = models.CharField(max_length=50, unique=True)
        quantity= models.IntegerField()
        price = models.DecimalField(max_digits=7, decimal_places=2)
        branch = models.ForeignKey(Branch, on_delete=models.SET_DEFAULT, null=True, blank=True, default=None)

        def __str__(self):
                return self.name
