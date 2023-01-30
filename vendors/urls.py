from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendor_home, name="vendor_home"),
    path('signup/', views.vendor_signup, name="vendor_signup"),
    path('signin/', views.vendor_signin, name="vendor_signin"),
    path('signout/', views.signout, name="vendor_signout"),
    path('v-profile/', views.vendor_profile,
         name="vendor_profile"),
    path('add-profile/', views.add_vendor_profile,
         name="add_vendor_profile"),
    path('view-scraps/', views.view_scraps,
         name="view_scraps"),
    path('select-scrap/<int:scrap_id>', views.select_scrap,
         name="select_scrap"),
    path('pickup-scrap/<int:scrap_id>', views.pickup_scrap,
         name="pickup_scrap"),
    path('my-orders/', views.orders,
         name="orders"),
    path('my-pickups/', views.view_pickups,
         name="view_pickups"),
]
