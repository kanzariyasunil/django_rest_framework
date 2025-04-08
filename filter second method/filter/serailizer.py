from rest_framework import serializers
from .models import OtherStudent


class Studentserialer(serializers.ModelSerializer):
    class Meta:
        model = OtherStudent
        fields = "__all__"