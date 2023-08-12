from django.db import models
from django.contrib.auth.models import User
from .in_choice import STATE_CHOICES,cities



class Location(models.Model):
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128,blank=True)
    city=models.CharField(choices=cities ,max_length=64)
    state = models.CharField(choices=STATE_CHOICES ,default='KL' ,blank=True,max_length=120)
    zip_code= models.CharField(max_length = 150)
  
    
    
    
    

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(null=False)
    bio = models.CharField(max_length=140,blank=True)
    phone_number = models.CharField(max_length=12 ,null=False)
    location=models.OneToOneField(
        Location,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f'{self.user.username}\'s profile'
        