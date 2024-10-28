# Ex02 Django ORM Web Application
## Date: 22.10.24

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Screenshot 2024-10-28 132747-1.png>)

## DESIGN STEPS

### STEP 1: 
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py
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

admin.py
from django.contrib import admin
from .models import Banker,BankerAdmin
admin.site.register(Banker,BankerAdmin)
```

## OUTPUT

![alt text](<Screenshot (1).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
