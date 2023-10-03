from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import App, ContactMessage
from .serializers import AppSerializer, ContactMessageSerializer

class AppViewSet(ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer

class ContactMessageViewSet(ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
