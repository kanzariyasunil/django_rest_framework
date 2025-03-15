from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student

# Create your views here.

class Stud(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    
class readonlyviewset(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer