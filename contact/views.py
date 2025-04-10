from django.shortcuts import render
from .import models, serializers
from rest_framework import viewsets
# Create your views here.


class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer