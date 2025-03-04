from django.urls import path
from .views import student_api, add_data, put_data, delete_data, Studentapiview
urlpatterns = [
    path("", student_api, name = "test api"),
    path("add", add_data, name = "Add data"),
    path("put", put_data, name = "put data"),
    path("delete", delete_data, name = "delete data"),
    path("apiview", Studentapiview.as_view(), name = "apiviwe data"),
]
