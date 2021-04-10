from django.db import models

# Create your models here.
class User(models.Model):
    Username=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    balance=models.IntegerField()
    password=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    

class Transfer(models.Model):
    To=models.CharField(max_length=30)
    From=models.CharField(max_length=30)
    amount=models.IntegerField()
    date=models.DateField()
    
    def __str__(self):
        return self.date
   
        
    