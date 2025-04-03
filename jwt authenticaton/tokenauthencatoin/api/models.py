from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField( max_length=50 )
    age = models.IntegerField()
    city = models.CharField( max_length=30 )

class Product(models.Model):
    product_name = models.CharField( max_length = 50)
    price = models.IntegerField()
    quentity = models.IntegerField()
    descriptions = models.CharField( max_length = 50)