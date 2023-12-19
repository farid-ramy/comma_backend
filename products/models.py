# products/models.py
from django.db import models
from branches.models import Branch

class Attribute(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Entity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    entity_name = models.CharField(max_length=255)
    attribute_name = models.CharField(max_length=50)
    attribute_value = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.SET_DEFAULT, null=True, blank=True, default=None)

    def save(self, *args, **kwargs):
        # Resolve the entity and attribute based on names before saving
        entity, _ = Entity.objects.get_or_create(name=self.entity_name)
        attribute, _ = Attribute.objects.get_or_create(name=self.attribute_name)
        self.entity_name = entity
        self.attribute_name = attribute
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.entity_name} - {self.attribute_name} - {self.attribute_value}"
