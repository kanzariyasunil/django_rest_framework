from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import 

# Create your views here.

class StudentViews(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    