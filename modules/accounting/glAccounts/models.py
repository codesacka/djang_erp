from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from modules.accounting.accountClass.models import AccountClass
# Create your models here.
class AccountGl (models.Model):
  name = models.CharField(max_length=300, default=0,null=True,blank=True)
  accountclass = models.ForeignKey(AccountClass,on_delete=models.CASCADE)
  manualentry = models.CharField(max_length=1, default=0,null=True,blank=True)
  glcode= models.CharField(max_length=300, default=0,null=True,blank=True)
  parent =models.IntegerField(default=0)
  description = models.TextField(null=True,blank=True)
  user         =models.ForeignKey(User,on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True,auto_now=False)
  updated_at = models.DateTimeField(auto_now_add=False,auto_now=True)

  class Meta:
        db_table = "gl_account"

        def __str__ (self):
            return  self.name
