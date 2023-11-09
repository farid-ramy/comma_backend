from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    role = models.CharField(max_length=50)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    
    phone = models.CharField(max_length=15, null=True, blank=True, unique=True, validators=[RegexValidator(regex=r'^\d{11}$', message=_("Enter a valid phone number."))])
    email = models.EmailField(max_length=50, null=True, blank=True, unique=True)
    
    national_id = models.CharField(max_length=14, null=True, blank=True, unique=True, validators=[RegexValidator(regex=r'^\d{14}$', message=_("Enter a valid national ID."))])
    age = models.PositiveIntegerField(null=True, blank=True)
    job = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

    # def get_user_with_branch(self):
    #     from branches.models import WorkingIN

    #     user_data = {
    #         'id': self.id,
    #         'first_name': self.first_name,
    #         'last_name': self.last_name,
    #         'username': self.username,
    #         'phone': self.phone,
    #         'email': self.email,
    #         'national_id': self.national_id,
    #         'age': self.age,
    #         'job': self.job,
    #         'address': self.address,
    #         'created_at': self.created_at,
    #         'modified_at': self.modified_at,
    #     }

    #     working_in_instance = WorkingIN.objects.filter(employee_id=self).first()

    #     if working_in_instance:
    #         branch_data = {
    #             'branch_id': working_in_instance.branch_id.id,
    #             'branch_name': working_in_instance.branch_id.name,
    #             'branch_address': working_in_instance.branch_id.address,
    #             'branch_phone': working_in_instance.branch_id.phone,
    #             'branch_opening_hours': working_in_instance.branch_id.opening_hours,
    #             'branch_created_at': working_in_instance.branch_id.created_at,
    #             'branch_modified_at': working_in_instance.branch_id.modified_at,
    #         }
    #         user_data['branch'] = branch_data

    #     return user_data
