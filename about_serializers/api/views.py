from django.shortcuts import render, HttpResponse
from .models import Student
from .serializers import Studentseriazer
from rest_framework.renderers import JSONRenderer

# Create your views here.

def student_details(request):
    stu_de = Student.objects.all()
    stu_ser = Studentseriazer(stu_de, many = True)
    json_data = JSONRenderer().render(stu_ser.data)
    return HttpResponse(json_data, content_type='applicaton/json')