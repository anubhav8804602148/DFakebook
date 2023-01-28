from django.urls import path, include
from .views import *

urlpatterns = [
    path("all_apps", show_select_application_page),
    path("delete/<app_id>", delete_app),
]