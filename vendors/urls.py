from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendor_home, name="vendor_home"),
    path('signup/', views.vendor_signup, name="vendor_signup"),
    path('signin/', views.vendor_signin, name="vendor_signin"),
    path('v-profile/', views.vendor_profile,
         name="vendor_profile"),
    path('add-profile/', views.update_vendor_profile,
         name="update_vendor_profile"),
]
