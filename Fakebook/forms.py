from django import forms
from django.core import validators


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50,
                               validators=[validators.RegexValidator("[A-Za-z0-9_]{3,50}")])
    password = forms.CharField(max_length=28)
    confirm_password = forms.CharField(max_length=28)
    email = forms.EmailField()
