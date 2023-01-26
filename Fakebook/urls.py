from django.urls import path, include
from ManageApplications import urls
from .views import show_register_page

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", show_register_page),
    path("application/", include(urls)),
]
