from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import OtherStudents
# Create your views here.

class Studentlist(ModelViewSet):
    queryset = OtherStudents.objects.all()
    serializer_class = StudentSerializer

class Student_list_view(ListAPIView):
    queryset = OtherStudents.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        print(self.request.user)
        return OtherStudents.objects.filter(name = self.request.user.username  )
    