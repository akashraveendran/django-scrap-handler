from django.forms import forms,TextInput,PasswordInput,ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Scrap


class UserAddForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]
        widgets = {
            'username': TextInput(attrs={'placeholder':'Enter Username'}),
            'first_name': TextInput(attrs={'placeholder':'Enter Firstname'}),
            'last_name': TextInput(attrs={'placeholder':'Enter Lastname'}),
            'email': TextInput(attrs={'placeholder':'Enter Email'}),
        }
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({'placeholder':"Enter Password"})
        self.fields["password2"].widget.attrs.update({'placeholder':"Confirm Password"})


class AddScrapForm(ModelForm):
    class Meta:
        model = Scrap
        fields = ["Username","Phone_number","Email","Address","City","State","Pin_code","Scrap_Image"]

        widgets = {
            'Username':TextInput(attrs={"class":"form-control"}),
            'Phone_number': TextInput(attrs={"class":"form-control"}),
            'Email': TextInput(attrs={"class":"form-control"}),
            'Address': TextInput(attrs={"class":"form-control"}),
            "City": TextInput(attrs={"class":"form-control"}),
            "State": TextInput(attrs={"class":"form-control"}),
            "Pin_code": TextInput(attrs={"class":"form-control"}),
        }