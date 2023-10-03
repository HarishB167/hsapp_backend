from django.db import models

# Create your models here.

class App(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255)
    logo_url = models.CharField(max_length=255)


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    