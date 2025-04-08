from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViews
router = DefaultRouter()

router.register('', StudentViews, basename='strudent api views ')

urlpatterns = [
    path('', include(router.urls), name='student api')
]
