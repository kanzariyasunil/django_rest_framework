from django.shortcuts import render
from .models import Student
from .serializer import StudentsSerialiers
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

# Create your views here.

class StudentViewsSets(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerialiers
    filter_backends = [ SearchFilter ]
    search_filter = ['city']
