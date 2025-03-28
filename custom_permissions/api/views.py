from .models import Student
from .serializer import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from .custome_authentication import MyPermissions
from rest_framework import viewsets

# Create your views here.

class studentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermissions]

