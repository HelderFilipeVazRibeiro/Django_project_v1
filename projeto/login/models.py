
# login/models.py

from django.db import models

class autentication(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)



class profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    birth_date = models.DateField()
    description = models.TextField()

class my_wallet(models.Model):
     budget = models.DecimalField(max_digits=10, decimal_places=2)
     start_date = models.DateField() 
     event_date = models.DateField() 

class Expense(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)