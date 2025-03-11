from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import StuentSerializer
from .models import Student

# Create your views here.

class StudentViewssets(ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serialzer = StuentSerializer(stu, many = True)
        return Response(serialzer.data)
    
    def create(self, request):
        ser = StuentSerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response({"massage":"success!"})
        else:
            return Response({"message":"unsuccessful!"})
    
    def retrive(self, request, pk):
        ser = StuentSerializer(Student.objects.get(id = int(pk)))
        return Response({"data":ser.data})
        
        