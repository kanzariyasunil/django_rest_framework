from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


# Create your views here.
class GenericApiview(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kawrgs):
        return self.list(request, *args, **kawrgs)
    

class Createapi(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kawrgs):
        return self.create(request, *args, **kawrgs)
    
class Retrivemodelmixin(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kawrgs):
        return self.retrieve(request, *args, **kawrgs)
    
class Updatedata(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kawrgs):
        return self.update(request, *args, **kawrgs)
    
class Deletedata(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kawrgs):
        return self.destroy(request, *args, **kawrgs)