from django.forms import forms,TextInput,PasswordInput,ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import VendorProfile


class VendorAddForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]

class AddVendorForm(ModelForm):
    class Meta:
        model = VendorProfile
        fields = ["shop_name","License_No","GST_No","Postcode","Phone_Number","Area","District","State","Profile_Image"]

        widgets = {
            'shop_name': TextInput(attrs={"class":"form-control","placeholder":"Shop Name"}),
            'License_No': TextInput(attrs={"class":"form-control","placeholder":"Licence Number"}),
            'GST_No': TextInput(attrs={"class":"form-control","placeholder":"GST No"}),
            'Postcode': TextInput(attrs={"class":"form-control","placeholder":"Postcode"}),
            'Phone_Number': TextInput(attrs={"class":"form-control","placeholder":"Phone Number"}),
            'Area': TextInput(attrs={"class":"form-control","placeholder":"Area/city"}),
            'District': TextInput(attrs={"class":"form-control","placeholder":"District"}),
            "State": TextInput(attrs={"class":"form-control","placeholder":"State"}),
        }