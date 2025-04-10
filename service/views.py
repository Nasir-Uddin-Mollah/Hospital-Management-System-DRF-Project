from django.shortcuts import render
from .import models, serializers
from rest_framework import viewsets
# Create your views here.


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer