from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('update-profile/', views.update_user_profile, name="update_user_profile"),
    path('select-scrap/', views.select_scrap, name="select_scrap"),
    path('confirm-scrap/<int:scrap_id>', views.confirm_scrap, name="confirm_scrap"),
]
