from django.db import models
from branches.models import Branch

class Package (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    offer = models.DecimalField(max_digits=7 , decimal_places=2,null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_DEFAULT, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)  

    class Meta:
        unique_together = ['branch', 'name']

    def __str__(self):
        return self.name
    
class PackageAttribute(models.Model):
    package= models.ForeignKey(Package, on_delete=models.CASCADE)
    attribute_name=models.CharField(max_length=50)
    attribute_value=  models.CharField(max_length=225)
    
    class meta:
        unique_together= ['package','attribute_name']   
    
    def __str__(self) :
        return f"{self.package}-{self.attribute_name}:{self.attribute_value}"    



