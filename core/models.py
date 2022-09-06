from django.db import models

# Create your models here.

class App(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255)
    logo_url = models.CharField(max_length=255)
