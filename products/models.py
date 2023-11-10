from django.db import models
from branches.models import Branch

# Create your models here.
class products (models.Model):
        name = models.CharField(max_length=50)
        quantity= models.IntegerField()
        price = models.DecimalField(max_digits=7, decimal_places=2)
        branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='productsBranch_id', default=None)


        def __str__(self):
                return self.name
