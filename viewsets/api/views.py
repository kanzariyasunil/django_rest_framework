from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import StuentSerializer
from .models import Student
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
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
        
    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = StuentSerializer(user)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        users = Student.objects.get(pk = pk)
        ser = StuentSerializer(users, data = request.data)
        if ser.is_valid():
            ser.save()
            return Response({"massage":"ok"})
        else:
            return Response({"Massage":"enter valid data"})

    def partial_update(self, request, pk=None):
        users = Student.objects.get(pk = pk)
        ser = StuentSerializer(users, data = request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"massage":"ok"})
        else:
            return Response({"Massage":"please valid data"})
        
    def destroy(self, request, pk=None):
        user = Student.objects.get(pk = pk) 
        user.delete()
        return Response({"Massage":"Data is deleted successfull!"})

@api_view(["DELETE"])
def deletedata(request):
    users = Student.objects.filter(city = request.data['city'])
    users.delete()
    return Response({"Massage":"success ful delete!"})