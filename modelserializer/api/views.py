from django.shortcuts import render
from .serializers import Studentserializer
from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def get(request):
    return Response(Studentserializer(Student.objects.all(), many = True).data)

@api_view(['POST'])
def post(request):
    ser = Studentserializer(data = request.data)

    if ser.is_valid():
        ser.save()
        return Response({"status":"success"})
    else:
        return Response({"status":"unsuccessful!"})
    
@api_view(["PUT"])
def PUT(request):
    ser = Studentserializer(Student.objects.get(id = request.data['id']), data = request.data)

    if ser.is_valid():
        ser.save()
        return Response({"status":"succefull"})
    else:
        return Response({'status':"There is something is wrong!"})

@api_view(["DELETE"])
def delete(request):
    ser = Student.objects.get(id = request.data['id'])
    ser.delete()
    return Response({"status":"data deleted succellful!"})