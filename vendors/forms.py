from django.forms import forms,TextInput,PasswordInput,ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import VendorProfile


class VendorAddForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]

class UpdateVendorForm(ModelForm):
    class Meta:
        model = VendorProfile
        fields = ["Phone_Number","Address","City","State","Profile_Image"]

        widgets = {
            'Phone_Number': TextInput(attrs={"class":"form-control"}),
            'Address': TextInput(attrs={"class":"form-control"}),
            "City": TextInput(attrs={"class":"form-control"}),
            "State": TextInput(attrs={"class":"form-control"}),
        }