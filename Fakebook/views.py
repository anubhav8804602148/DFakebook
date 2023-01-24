from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.auth.models import User
from logger.Logger import Logger
from django.contrib.auth.hashers import make_password

REGISTER_PAGE = "registration/register.html"
LOGIN_PAGE = "registration/login.html"
logger = Logger("fakebook_logger.log")


def show_register_page(request):
    logger.log_request(request)

    if request.method == 'GET':
        return render(request, REGISTER_PAGE, {"form": RegistrationForm()})

    if request.method == 'POST':
        if request.POST.get('password') != request.POST.get('confirmPassword'):
            return render(request, REGISTER_PAGE, {
                "form": request.POST,
                "error": "Password should match confirm password"
            })

        user = User()
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.password = make_password(request.POST.get('password'))
        user.save()
        return render(request, LOGIN_PAGE)
    return render(request, REGISTER_PAGE)
