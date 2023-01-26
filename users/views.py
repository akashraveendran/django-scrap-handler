from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

from .forms import UserAddForm
from .decorators import user_only, not_auth_user

from .models import Scrap

# Create your views here.


def home(request):
    return render(request, "home.html")


@user_only
def index(request):
    return render(request, "users/user-home.html")


@not_auth_user
def signup(request):  # first get the user form from forms.py to render with signup.html
    signup_form = UserAddForm()
    if(request.method == "POST"):
        form = UserAddForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("password")
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken !!! Retry")
                return redirect("signup")
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken !!! Retry")
                return redirect("signup")
            else:
                new_user = form.save()
                new_user.save()

                # getting and assigning group to the user
                group = Group.objects.get(name="user")
                new_user.groups.add(group)
                messages.info(request, "User Created")
                return redirect("signin")
        else:
            messages.info(
                request, "Fom validation Failed!!! Try a defferent password.")

    return render(request, "users/signup.html", {"signup_form": signup_form})


@not_auth_user
def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session["username"] = username
            request.session["password"] = password
            login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Username or password incorrect ")
            return redirect("signin")
    return render(request, "users/signin.html")


def signout(request):
    logout(request)
    return redirect("signin")


def update_user_profile(request):
    return render(request, "users/update-user.html")

def select_scrap(request):
    
    if request.method == "POST":
        waste_type = " , ".join(request.POST.getlist("waste_type[]"))
        user = User.objects.get(id=request.user.id)
        scrap = Scrap.objects.create(waste_type=waste_type,user_ID=user)
        return redirect("confirm_scrap",scrap.id)

    return render(request, "users/scrap_selecter.html")


def confirm_scrap(request,scrap_id):
    if request.method == "POST":
        scrap = Scrap.objects.filter(id=request.POST["id"]).update(username=request.POST["username"])
        print(request.POST["id"],request.POST["username"])
    return render(request, "users/s_confirm.html",{"id":scrap_id})
