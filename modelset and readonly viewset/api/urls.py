from django.urls import path, include
from .views import Stud, readonlyviewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("student", Stud, basename="student")
router.register("readonly", readonlyviewset, basename="readonly")

urlpatterns = [
    path("", include(router.urls))
]
