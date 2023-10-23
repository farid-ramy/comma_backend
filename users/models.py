from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Custom validator for email format
email_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$',
    message=_("Enter a valid email address."),
)

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    
    email = models.EmailField(max_length=50, null=True, blank=True, unique=True, validators=[email_validator])
    phone = models.CharField(max_length=15, null=True, blank=True, unique=True, validators=[RegexValidator(regex=r'^\d{10,15}$', message=_("Enter a valid phone number."))])
    
    job = models.CharField(max_length=15, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=50)
    national_id = models.CharField(max_length=20, null=True, blank=True, unique=True, validators=[RegexValidator(regex=r'^\d{10,20}$', message=_("Enter a valid national ID."))])


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
