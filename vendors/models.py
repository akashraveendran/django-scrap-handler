from django.db import models

from django.contrib.auth.models import User


# Create your models here.




class VendorProfile(models.Model):
    Vendor_ID = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True )
    First_name = models.CharField(max_length=200,null=True,blank=True)
    Surname = models.CharField(max_length=200,null=True,blank=True)
    shop_name = models.CharField(max_length=200,null=True,blank=True)
    License_No = models.CharField(max_length=200,null=True,blank=True)
    GST_No = models.CharField(max_length=200,null=True,blank=True)
    Postcode = models.CharField(max_length=200,null=True,blank=True)
    Email = models.CharField(max_length=200,null=True,blank=True)
    Phone_Number = models.CharField(max_length=200,null=True,blank=True)
    Area = models.CharField(max_length=200,null=True,blank=True)
    District = models.CharField(max_length=200,null=True,blank=True)
    State = models.CharField(max_length=200,null=True,blank=True)
    Profile_Image = models.ImageField(upload_to="vendors",null=True,blank=True)