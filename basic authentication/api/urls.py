from django.urls import path, include
from .views import Stud
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("student", Stud, basename="student")


urlpatterns = [
    path("", include(router.urls))
]
