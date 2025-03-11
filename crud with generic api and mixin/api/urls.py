from django.urls import path
from .views import ClrModel, Rdumodel
urlpatterns = [
    # this model is only support for create and read 
    path("", ClrModel.as_view(), name = "read and create model"),
    path("rud/<int:pk>", Rdumodel.as_view(), name = "update, delete and retrive model")
]
