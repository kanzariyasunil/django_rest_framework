from django.urls import path
from .views import create, getview
urlpatterns = [
    path("", create, name = "path"),
    path("get", getview, name = "path")
]
