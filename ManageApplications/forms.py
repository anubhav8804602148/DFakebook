from django import forms


class AppForm(forms.Form):
    application_name = forms.CharField(max_length=50)
    application_path = forms.CharField(max_length=200)
    application_logo = forms.ImageField()
