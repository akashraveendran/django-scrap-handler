from django.db import models

from django.contrib.auth.models import User


# Create your models here.




class VendorProfile(models.Model):
    Vendor_ID = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True )
    Address = models.CharField(max_length=200,null=True,blank=True)
    City = models.CharField(max_length=200,null=True,blank=True)
    State = models.CharField(max_length=200,null=True,blank=True)
    Phone_Number = models.CharField(max_length=200,null=True,blank=True)
    Profile_Image = models.ImageField(upload_to="vendors",null=True,blank=True)