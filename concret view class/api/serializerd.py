from rest_framework import serializers
from .models import Student

# here student serializer class are define

class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Student
        fields = "__all__"