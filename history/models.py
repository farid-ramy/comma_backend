from django.db import models
from users.models import User
from branches.models import Branch

class History(models.Model):
   client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_id')
   # employee = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='employee' , null=True)
   # branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='branch')
   # check_in_time = models.DateTimeField(auto_now_add=True)
   # check_out_time = models.DateTimeField(null=True, blank=True)
   # payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

   # def __str__(self):
   #    return f"{self.client.first_name} -> {self.check_in_time.strftime('%Y-%m-%d %H:%M:%S')}"
   
