import django.contrib.auth.views
from django.urls import path, include
from.views import *
urlpatterns = [
    path("", show_chat_home)
]
