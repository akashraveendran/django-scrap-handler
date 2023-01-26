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
    username = models.CharField(max_length=200,null=True,blank=True)
    user_email = models.CharField(max_length=200,null=True,blank=True)
    user_phone = models.CharField(max_length=200,null=True,blank=True)
    user_address = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    state = models.CharField(max_length=200,null=True,blank=True)
    pin = models.CharField(max_length=200,null=True,blank=True)
    scrap_image = models.ImageField(upload_to="scraps",null=True,blank=True)
    
