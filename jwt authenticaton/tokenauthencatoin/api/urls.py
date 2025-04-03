from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter
from .views import StudentViews
router = DefaultRouter()

router.register("", StudentViews, basename='Student api')

urlpatterns = [
    path("", include(router.urls)),
    path('gettoken', TokenObtainPairView.as_view(), name='token obtaion view'),
    path('refreashtoekn', TokenRefreshView.as_view(), name='tokenrefresh view'),
    path('verifytoken', TokenVerifyView.as_view(), name='tokenverify view')
]