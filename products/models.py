from django.db import models
from branches.models import Branch

class Product(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    branch = models.ForeignKey(Branch, on_delete=models.SET_DEFAULT, null=True, blank=True, default=None)

    class Meta:
        unique_together = ['branch', 'name']

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute_name = models.CharField(max_length=50)
    attribute_value = models.CharField(max_length=255)

    class Meta:
        unique_together = ['product', 'attribute_name']

    def __str__(self):
        return f"{self.product} - {self.attribute_name}: {self.attribute_value}"
