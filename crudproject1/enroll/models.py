from django.db import models

# Create your models here.
class User(models.Model):
    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    mobile= models.CharField(max_length=15, default="")
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='Male')
    document = models.FileField(upload_to='documents/', blank=True)  # Update here
class Userlogin(models.Model):
    email=models.EmailField(max_length=100)
    password= models.CharField(max_length=15)