from django.urls import path
from .views import HomeInfoList, HomeInfoDetails
urlpatterns = [
    path('homeinfo/', HomeInfoList.as_view()),
    path('homedetails/<int:pk>/', HomeInfoDetails.as_view()),
]