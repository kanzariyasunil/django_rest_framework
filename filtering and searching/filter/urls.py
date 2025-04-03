from django.urls import path, include
from .views import Studentlist, Student_list_view
from rest_framework import routers

router = routers.DefaultRouter()

router.register("", Studentlist, basename="studnt api make for user!")

urlpatterns = [
    path('', include(router.urls) , name = "student list"),
    path('std', Student_list_view.as_view(), name = 'std')
]
