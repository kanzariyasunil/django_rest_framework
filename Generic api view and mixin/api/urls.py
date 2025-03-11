from django.urls import path
from .views import GenericApiview, Createapi, Retrivemodelmixin, Updatedata, Deletedata
urlpatterns = [
    path('', GenericApiview.as_view(), name="Generic api view" ),
    path('create', Createapi.as_view(), name="Generic api create" ),
    path('retrive/<int:pk>', Retrivemodelmixin.as_view(), name="Generic api retirve" ),
    path('update/<int:pk>', Updatedata.as_view(), name="Generic api update" ),
    path('delete/<int:pk>', Deletedata.as_view(), name="Generic api delete" ),
]
