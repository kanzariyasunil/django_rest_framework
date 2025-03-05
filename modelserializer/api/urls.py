from django.urls import path
from .views import get, post, PUT, delete
urlpatterns = [
    path("", get, name="get name"),
    path("post", post, name="post name"),
    path("put", PUT, name="put"),
    path("delete", delete, name="delete")
]
