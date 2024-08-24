from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    mobile= models.CharField(max_length=15, default="")
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    
class Userlogin(models.Model):
    email=models.EmailField(max_length=100)
    password= models.CharField(max_length=15)