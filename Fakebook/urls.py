from django.contrib import admin
from django.urls import path, include
from .views import show_register_page
urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", show_register_page),
]
