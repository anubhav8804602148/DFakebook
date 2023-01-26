from django.db import models


class App(models.Model):
    application_id = models.BigIntegerField()
    application_name = models.CharField(max_length=50)
    application_url = models.CharField(max_length=200)
    application_logo = models.CharField(max_length=200)
