from django.urls import path
from .views import allvalueget
urlpatterns = [
    path('student', allvalueget, name='student')
]