from django.db import models

from django.contrib.auth.models import User

# Create your models here.

# Create your models here.


class UserProfileList(models.Model):
    user_ID = models.AutoField(primary_key=True)
    user_address = models.CharField(max_length=200)
    user_location = models.CharField(max_length=200)
    Profile_Image = models.ImageField(upload_to="user_images")



class Scrap(models.Model):
    user_ID =models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    waste_type = models.CharField(max_length=200)
    Username = models.CharField(max_length=200,null=True,blank=True)
    Email = models.CharField(max_length=200,null=True,blank=True)
    Phone_number = models.CharField(max_length=200,null=True,blank=True)
    Address = models.CharField(max_length=200,null=True,blank=True)
    City = models.CharField(max_length=200,null=True,blank=True)
    State = models.CharField(max_length=200,null=True,blank=True)
    Pin_code = models.CharField(max_length=200,null=True,blank=True)
    Scrap_Image = models.ImageField(upload_to="scraps",null=True,blank=True)
    status = models.CharField(max_length=200,null=True,blank=True)
    
