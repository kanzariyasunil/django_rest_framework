from django.shortcuts import render, HttpResponse
from .models import Student
from .serializers import Studentserialier
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['POST'])
def create(request):
    serializer = Studentserialier(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return HttpResponse({"massage":"success"})
    else:
        return HttpResponse("Some error are occured!")
    
@api_view(["GET"])
def getview(request):
    return Response(Studentserialier(Student.objects.all(), many = True).data if Studentserialier(Student.objects.all(), many = True) else "No data here")



