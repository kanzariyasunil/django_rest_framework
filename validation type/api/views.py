from django.shortcuts import render
from .models import Student
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(["GET"])
def get(request):
    return Response(StudentSerializer(Student.objects.all(), many = True).data)

@api_view(["POST"])
def post(request):
    ser = StudentSerializer(data = request.data)
    if ser.is_valid():
        ser.save()
        return Response({"massage":"success full added!"})
    else:
        return Response({"meassge":ser.errors})