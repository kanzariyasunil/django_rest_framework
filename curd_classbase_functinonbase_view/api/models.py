from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField(default=6)
    city = models.CharField(max_length=50)
