from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    age = serializers.IntegerField(default=6)
    city = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        instance.city = validated_data.get("city", instance.city)
        instance.save()

        return instance
    