from django.urls import path
from .views import HomeInfoList, HomeInfoDetails, homeinfo, homedata, home_data

urlpatterns = [
    path('homeinfo/', HomeInfoList.as_view()),
    path('homedetails/<int:pk>/', HomeInfoDetails.as_view()),
    path('home/', homeinfo, name='home'),
    path('homedata/', home_data)
]
