from django.db import models


class App(models.Model):
    application_Id = models.AutoField(primary_key=True)
    application_name = models.CharField(max_length=50)
    application_path = models.CharField(max_length=200)
    application_logo = models.ImageField(upload_to="static/media/images/")
