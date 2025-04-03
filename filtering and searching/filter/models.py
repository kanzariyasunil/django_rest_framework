from django.db import models

# Create your models here.

class OtherStudents(models.Model):
    name = models.CharField( max_length=20)
    roll = models.IntegerField(auto_created=True)
    city = models.CharField( max_length=30)
    passby = models.IntegerField()


    