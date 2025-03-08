from django.urls import path
from .views import StudentModelViewSet
urlpatterns = [
    path("", StudentModelViewSet.as_view({'get': 'list'}), name="as view for serializer")
]
