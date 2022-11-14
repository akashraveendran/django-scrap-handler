from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import UserAddForm

# Create your views here.


def index(request):
    return render(request, "index.html")


def signup(request):  # first get the user form from forms.py to render with signup.html
    signup_form = UserAddForm()
    if(request.method == "POST"):
        form = UserAddForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("password")
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect("signup")
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect("signup")
            else:
                new_user = form.save()
                new_user.save()
                messages.info(request, "User Created")
                return redirect("signin")
    return render(request, "signup.html", {"signup_form": signup_form})


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session["username"] = username
            request.session["password"] = password
            login(request, user)
            return redirect("HomeScreen")
        else:
            messages.info(request, "Username or password incorrect ")
            return redirect("Signin")
    return render(request, "signin.html")
