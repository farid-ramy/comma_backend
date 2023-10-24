from django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class Branch(models.Model):
    name = models.CharField(max_length=50, unique=True, validators=[RegexValidator(regex=r'^[A-Za-z\s]+$', message="Enter a valid name.")])
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    manager_name = models.CharField(max_length=50, blank=True)
    opening_hours = models.CharField(max_length=100, blank=True)
    established_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name