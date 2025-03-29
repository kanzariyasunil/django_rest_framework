from .models import Student
from .serializer import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework import viewsets

# Create your views here.

class studentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    
