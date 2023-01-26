import logging

from django.shortcuts import render, redirect
from util.Parser import request_data_to_user
from .forms import RegistrationForm
from util.Logger import Logger
from util.UserValidator import MSG_USERDATA_VALID

REGISTER_PAGE = "registration/register.html"
LOGIN_PAGE = "registration/login.html"
logger = Logger("fakebook.log")


def show_login_page(request, redirect_params=None):
    logger.log_request(request)
    return render(request, LOGIN_PAGE, redirect_params)


def show_register_page(request):
    logger.log_request(request)

    if request.method == 'GET':
        return render(request, REGISTER_PAGE, {"form": request.GET})

    if request.method == 'POST':
        try:
            validation_message = RegistrationForm(request.POST).validate()
            if validation_message == MSG_USERDATA_VALID:
                request_data_to_user(request.POST).save()
                return redirect("login")
        except Exception as err:
            validation_message = str(err)
            logging.log(0, err)
        return render(request, REGISTER_PAGE, {
            "form": request.POST,
            "message": validation_message,
            "color": "red"
        })
    return render(request, REGISTER_PAGE, {
        "message": "Only GET and POST methods allowed. Are you debugging?",
        "color": "orange"
    })
