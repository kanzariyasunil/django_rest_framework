from django.urls import path
from .views import StudentList, StudentCreate, StudentDelete, StudentRetrive, StudentUpdate,Createlists, Retriveupdatedelete, Retriveupdate, RetrieveDestroyAPIView
urlpatterns = [
    path("", StudentList.as_view(), name = "Student api"),
    path("create", StudentCreate.as_view(), name = "Student api"),
    path("createlists", Createlists.as_view(), name = "Student create and read"),
    path("delete/<int:pk>", StudentDelete.as_view(), name = "Student delete"),
    path("update/<int:pk>", StudentUpdate.as_view(), name = "Student update"),
    path("retrive/<int:pk>", StudentRetrive.as_view(), name = "Student retrive"),
    path("retriveupdatedelete/<int:pk>", Retriveupdatedelete.as_view(), name = "Student retrive, update and delete"),
    path("retriveupdate/<int:pk>", Retriveupdate.as_view(), name = "Student retrive and update"),
    path("retrieveDestroyAPIView/<int:pk>", RetrieveDestroyAPIView.as_view(), name = "Student retrive and destroy"),
]
