import django.contrib.auth.views
from django.urls import path, include
from ManageApplications import urls as manage_application_urls
from ProfileManagement import urls as profile_management_urls
from ChatBox import urls as chatbox_urls
from .views import show_register_page


handler404 = 'Fakebook.views.handler404'
handler500 = 'Fakebook.views.handler500'

urlpatterns = [
    path("login/", django.contrib.auth.views.LoginView.as_view()),
    path("logout/", django.contrib.auth.views.LogoutView.as_view()),
    path("register/", show_register_page),
    path("application/", include(manage_application_urls)),
    path("ProfileManagement/", include(profile_management_urls)),
    path("ChatBox/", include(chatbox_urls)),
    path("", manage_application_urls.show_select_application_page),
]
