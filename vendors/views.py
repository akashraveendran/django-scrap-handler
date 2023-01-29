from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from users.forms import UserAddForm

from .decorators import not_auth_vendor, vendor_only

from .forms import AddVendorForm
from .models import VendorProfile
from users.models import Scrap

# Create your views here.


@vendor_only
def vendor_home(request):
    return render(request, "vendors/vendor-home.html")


@not_auth_vendor
def vendor_signup(request):  # first get the user form from forms.py to render with signup.html
    signup_form = UserAddForm()
    if(request.method == "POST"):
        form = UserAddForm(request.POST)
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
    return redirect("vendor_signin")

@vendor_only
def add_vendor_profile(request):
    add_form = AddVendorForm()
    if request.method == "POST":
        add_form = AddVendorForm(request.POST,request.FILES)
        if(add_form.is_valid()):
            vendor = User.objects.get(id=request.user.id)
            updated_profile = add_form.save()
            updated_profile.Vendor_ID = vendor
            updated_profile.First_name = request.user.first_name
            updated_profile.Surname = request.user.last_name
            updated_profile.Email = request.user.email
            updated_profile.save()
            return redirect("vendor_profile")
    return render(request, "vendors/add-vendor.html",{"add_form":add_form})

@vendor_only
def vendor_profile(request):
    v_profile = VendorProfile.objects.filter(Vendor_ID=request.user.id)
    print(len(v_profile))
    if(len(v_profile) == 0):
        return redirect("add_vendor_profile")
    else:
        return render(request, "vendors/vendor-profile.html",{"v_profile":v_profile})


@vendor_only
def view_scraps(request):
    scraps = Scrap.objects.filter(status="Added")
    return render(request, "vendors/view-scraps.html",{"scraps":scraps})

    
@vendor_only
def select_scraps(request,scrap_id):
    scrap = Scrap.objects.get(id=scrap_id)
    scrap.status = "Selected"
    return redirect("view_scraps")

