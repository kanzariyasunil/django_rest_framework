from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import studentModelViewset
from rest_framework.authtoken.views import obtain_auth_token 
router = DefaultRouter()

router.register("Student", studentModelViewset, basename="Student base set")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include('rest_framework.urls')),
    path('gettoken/', obtain_auth_token)
]
