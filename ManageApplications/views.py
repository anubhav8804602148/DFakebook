import os

from django.shortcuts import render, redirect

from .forms import AppForm
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
            "app_list": App.objects.all(),
            "form": AppForm()
        })
    elif request.method == "POST":
        logger.log_request(request)
        logger.log(request.FILES)
        try:
            app_form = AppForm(request.POST, request.FILES)
            app_form.is_valid()
            App.objects.create(
                application_name=app_form.cleaned_data['application_name'],
                application_path=app_form.cleaned_data['application_path'],
                application_logo=app_form.cleaned_data['application_logo']
            ).save()
        except Exception as exc:
            logger.log(exc)
            return render(request, SELECT_APPLICATION_PAGE, {
                "app_list": App.objects.all(),
                "message": exc,
                "color": "red"
            })
    return render(request, SELECT_APPLICATION_PAGE, {
        "app_list": App.objects.all()
    })


def delete_app(request, app_id):
    logger.log_request(request)
    if not request.user.is_authenticated:
        return redirect("/login")
    if request.method == "POST":
        logger.log("Delete Id : {}".format(app_id))
        try:
            app = App.objects.get(application_Id=app_id)
            os.remove(str(app.application_logo))
            app.delete()
            return redirect("/application/all_apps")
        except BaseException as err:
            logger.log(err)
