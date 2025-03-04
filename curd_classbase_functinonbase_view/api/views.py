from django.shortcuts import render, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from .models import Student
from .serailizers import StudentSerializer
from rest_framework.decorators import api_view, APIView
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# Its call function base views

def student_api(request):
    if request.method == "POST":
        json_data = request.body()
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id", None)

        if id:
            stu = Student.objects.all(id = id)
            serializer = StudentSerializer(stu, many = True)
            json_data = JSONRenderer().render(serializer)
            return HttpResponse(json_data if json_data else "none")
    stu = Student.objects.all()
    ser = StudentSerializer(stu, many = True)
    
    return HttpResponse(ser.data)


@api_view(["POST"])
def add_data(request):
    serializer = StudentSerializer(data = request.data)

    if serializer.is_valid(raise_exception = True):
        serializer.save()
        return HttpResponse("your data will be added")
    else:
        return HttpResponse("Somthing want wrong please try leter!")
    
@api_view(["PUT"])
def put_data(request):
    student = Student.objects.get(id = request.data['id'])
    ser = StudentSerializer(student, data = request.data)

    if ser.is_valid():
        ser.save()
        return HttpResponse("yout data will be updated!")
    else:
        return HttpResponse("There are some issue: ", ser.errors)

@api_view(["DELETE"])
def delete_data(request):
    try:
        Student.objects.get(id = request.data['id']).delete()
        return HttpResponse("Data is successfully deleted!")
    except:
        return HttpResponse("somting wrong or may be data is not found!")
    
# class base views


class Studentapiview(APIView):
    def get(self, request):
        return HttpResponse(StudentSerializer(Student.objects.all(), many = True).data)
        
    def post(self, request):
        ser = StudentSerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return HttpResponse("congres your data will added!")
        else:
            return HttpResponse(f"you have add some wrong infoamation please currect this {ser.errors}")