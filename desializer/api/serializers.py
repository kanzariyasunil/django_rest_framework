from rest_framework import serializers
from .models import Student
class Studentserialier(serializers.Serializer):
    name = serializers.CharField(max_length=50)    
    city = serializers.CharField(max_length=50)    
    age = serializers.IntegerField()

    def create(self, validate_data):
        return Student.objects.create(**validate_data)