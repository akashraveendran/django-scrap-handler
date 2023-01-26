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
    path('confirm-scrap/<str:waste_type>', views.confirm_scrap, name="confirm_scrap"),
    path('view-my-scraps/', views.view_my_scraps, name="view_my_scraps"),
    path('delete-my-scrap/<int:id>', views.delete_scrap, name="delete_scrap"),
]
