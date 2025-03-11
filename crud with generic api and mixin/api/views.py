from django.shortcuts import HttpResponse
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin,  RetrieveModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.generics import GenericAPIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.

# there are created two in one api key: listModelmixin, CreateModelMixin

class ClrModel(GenericAPIView,  ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    add = []
    count = 0
    def get(self, request, *args, **kwargs):
       return self.list(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Now retrivemodel, destroymodel and updatemodels needs pk value 

class Rdumodel(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return HttpResponse(e)