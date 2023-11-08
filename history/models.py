from django.db import models
from users.models import User
from branches.models import Branch

<<<<<<< HEAD
class History (models.Model):
     client_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checkins',to_field='id',blank=True,null=True)
     branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE,to_field='id',default=None,blank=True,null=True)
     employee_id = models.ForeignKey(User, on_delete=models.CASCADE,to_field='id', default=None,blank=True,null=True,related_name='checkouts')

     checkin_time = models.DateTimeField(auto_now_add=True)
     checkout_time = models.DateTimeField(null=True,blank = True)
     price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
     
     
     def __str__(self):
        return f"Check-in for {self.client.username} at {self.branch.name}"
=======
class History(models.Model):
   client_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id', related_name='checkins')
   employee_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id', related_name='checkouts')
   branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, to_field='id')
   checkin_time = models.DateTimeField(auto_now_add=True)
   checkout_time = models.DateTimeField(null=True, blank=True)
   price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

   def __str__(self):
      return f"{self.client_id.first_name} {self.checkin_time.strftime('%d/%m/%Y %H:%M')}"
>>>>>>> f8752a7950c5100d3975743722e10dbde455a2e1

