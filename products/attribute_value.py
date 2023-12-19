from django.db import models
from .entity import Entity
from .attribute import Attribute

class AttributeValue(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ['entity', 'attribute']

    def __str__(self):
        return f"{self.entity.name} - {self.attribute.name}: {self.value}"