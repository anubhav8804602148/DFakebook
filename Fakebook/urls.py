import django.contrib.auth.views
from django.urls import path, include
from ManageApplications import urls
from .views import show_register_page

urlpatterns = [
    path("login/", django.contrib.auth.views.LoginView.as_view()),
    path("logout/", django.contrib.auth.views.LogoutView.as_view()),
    path("register/", show_register_page),
    path("application/", include(urls)),
]
