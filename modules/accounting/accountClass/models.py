from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class AccountClass (models.Model):
  name = models.CharField(max_length=300, default=0,null=True,blank=True)
  user     =models.ForeignKey(User,on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True,auto_now=False)
  updated_at = models.DateTimeField(auto_now_add=False,auto_now=True)

  class Meta:
        db_table = "account_class"

        def __str__ (self):
            return  self.name