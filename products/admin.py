# products/admin.py
from django.contrib import admin
from .models import Attribute, Entity, Product

admin.site.register(Attribute)
admin.site.register(Entity)
admin.site.register(Product)
