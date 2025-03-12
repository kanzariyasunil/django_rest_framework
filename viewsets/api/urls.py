from django.urls import path, include
from .views import StudentViewssets, deletedata
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('studentapi', StudentViewssets, basename="studentapi")

urlpatterns = [
    path("deletedata", deletedata, name=" delete data using filter methods"),
    path("", include(router.urls))
]
