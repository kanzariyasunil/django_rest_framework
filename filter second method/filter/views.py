from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import OtherStudent
from .serailizer import Studentserialer
# from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class StudentViews(ModelViewSet):
    queryset = OtherStudent.objects.all()
    serializer_class = Studentserialer
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city']
