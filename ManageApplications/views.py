from django.shortcuts import render, redirect
from .models import App
from util.Logger import Logger

LOGIN_PAGE = "registration/login.html"
SELECT_APPLICATION_PAGE = "all_apps.html"
logger = Logger("fakebook.log")


def show_select_application_page(request):
    logger.log_request(request)
    if not request.user.is_authenticated:
        return redirect("/login")
    if request.method == "GET":
        return render(request, SELECT_APPLICATION_PAGE, {
            "message": "",
            "app_list": App.objects.all()
        })
