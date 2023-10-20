from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)  # You should hash and secure passwords, not store them in plain text
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)  # You can adjust the max_length as needed
    age = models.PositiveIntegerField(blank=True, null=True)
    job = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    role = models.CharField(max_length=50)
    national_id = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name  # Return a user-friendly string representation of the user

# Add any additional methods or properties you need for the User model
