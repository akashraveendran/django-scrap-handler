from django.db import models

# Create your models here.


class ProfilesList(models.Model):
    Vendor_ID = models.AutoField(primary_key=True)
    Vendor_address = models.CharField(max_length=200)
    Vendor_location = models.CharField(max_length=200)
