from django.shortcuts import render

# Create your views here.


def vendor_home(request):
    return render(request, "vendor-home.html")
