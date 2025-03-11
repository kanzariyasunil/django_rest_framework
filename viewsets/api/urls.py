from django.urls import path, include
from .views import StudentViewssets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('studentapi', StudentViewssets, basename="studentapi")

urlpatterns = [
    path("", include(router.urls))
]
