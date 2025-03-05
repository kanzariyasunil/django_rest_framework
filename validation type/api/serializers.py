from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    city = serializers.CharField()

    def create(self, validated_data):
        return validated_data

    # it's call field level validations.
    def validate_age(self,request):
        if request < 7 or request > 40:
            raise  ValidationError("you are not eligable for admmition!")
        return request
    
    # it's call validators
    def validate(self, data):
        name = [i.isdigit() for i in data['name']]
        city = [i.isdigit() for i in data['city']]
        if name or city:
            raise ValidationError("you can not enter your name as digit!")
        return data