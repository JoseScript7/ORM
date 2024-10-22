
from django.db import models
from django.contrib import admin

class Banker(models.Model):
   account_holder_name=models.CharField(max_length=100)
   account_number=models.IntegerField(primary_key="account_number")
   ifsc_code=models.CharField(max_length=11)
   branch_name=models.CharField(max_length=100)
   email_id=models.EmailField()
   contact_number=models.IntegerField()
   salary=models.IntegerField()

class BankerAdmin(admin.ModelAdmin):
   list_display=('account_holder_name','account_number','ifsc_code','branch_name','email_id','contact_number','salary')
