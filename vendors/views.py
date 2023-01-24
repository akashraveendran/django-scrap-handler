from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from .forms import VendorAddForm

from .decorators import not_auth_vendor, vendor_only

# Create your views here.


@vendor_only
def vendor_home(request):
    return render(request, "vendors/vendor-home.html")


@not_auth_vendor
def vendor_signup(request):  # first get the user form from forms.py to render with signup.html
    signup_form = VendorAddForm()
    if(request.method == "POST"):
        form = VendorAddForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("password")
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken !!! Retry")
                return redirect("vendor_signup")
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken !!! Retry")
                return redirect("vendor_signup")
            else:
                new_user = form.save()
                new_user.save()

                # getting and assigning group to the user
                group = Group.objects.get(name="vendor")
                new_user.groups.add(group)
                messages.info(request, "Vendor Created")
                return redirect("vendor_signin")
        else:
            messages.info(
                request, "Fom validation Failed!!! Try a defferent password.")

    return render(request, "vendors/vendor-signup.html", {"signup_form": signup_form})


@not_auth_vendor
def vendor_signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session["username"] = username
            request.session["password"] = password
            login(request, user)
            return redirect("vendor_home")
        else:
            messages.info(request, "Username or password incorrect ")
            return redirect("vendor_signin")
    return render(request, "vendors/vendor-signin.html")


def signout(request):
    logout(request)
    return redirect("signin")


def update_vendor_profile(request):
    return render(request, "vendors/update-vendor.html")
