from django.db import models

# Create your models here.

# Create your models here.


class UserProfileList(models.Model):
    user_ID = models.AutoField(primary_key=True)
    user_address = models.CharField(max_length=200)
    user_location = models.CharField(max_length=200)
    Profile_Image = models.ImageField(upload_to="user_images")
