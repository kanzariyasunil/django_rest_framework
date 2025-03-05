from django.urls import path
from .views import get, post
urlpatterns = [
    path('', get, name="get request"),
    path('add',post, name="post")
    ]
