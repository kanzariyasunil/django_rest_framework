from rest_framework import serializers
from .models import OtherStudents

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherStudents
        fields = ['name', 'roll', 'passby', 'city']

    