from homeinfo.models import HomeInfo
from homeinfo.serializers import HomeInfoSerializer, HomeSerializer
from django.shortcuts import render

from rest_framework import generics


class HomeInfoList(generics.ListCreateAPIView):
    queryset = HomeInfo.objects.all()
    serializer_class = HomeSerializer


class HomeInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomeInfo.objects.all()
    serializer_class = HomeSerializer
