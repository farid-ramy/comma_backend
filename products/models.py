from django.db import models
from .attribute import Attribute
from branches.models import Branch
from .entity import Entity

class Product(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    attributes = models.ManyToManyField(Attribute, through='ProductAttributeValue')
    branch = models.ForeignKey(Branch, on_delete=models.SET_DEFAULT, null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ['product', 'attribute']

    def __str__(self):
        return f"{self.product.name} - {self.attribute.name}: {self.value}"
