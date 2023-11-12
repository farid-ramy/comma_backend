from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from branches.models import Branch

class User(models.Model):
    role = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True, unique=True, validators=[RegexValidator(regex=r'^\d{11}$', message=_("Enter a valid phone number."))])
    email = models.EmailField(max_length=50, null=True, blank=True, unique=True)
    national_id = models.CharField(max_length=14, null=True, blank=True, unique=True, validators=[RegexValidator(regex=r'^\d{14}$', message=_("Enter a valid national ID."))])
    job = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(max_length=100, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_DEFAULT, null=True, blank=True, default=None)
    created_by = models.ForeignKey('self', on_delete=models.SET_DEFAULT, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"