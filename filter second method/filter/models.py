from django.db import models

# Create your models here.
class OtherStudent(models.Model):
    name = models.CharField( max_length = 30)
    roll = models.IntegerField()
    city = models.CharField( max_length = 30)
    passby = models.IntegerField( )