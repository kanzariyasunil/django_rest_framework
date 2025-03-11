from rest_framework  import serializers
from .models import Student


# create a serializer 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name', 'age', 'city']
                