from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter
from .views import StudentViews
router = DefaultRouter()

router.register("", StudentViews, basename='Student api')

urlpatterns = [
    path("", include(router.urls))
]
