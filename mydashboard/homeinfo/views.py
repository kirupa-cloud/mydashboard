from homeinfo.models import HomeInfo
from homeinfo.serializers import HomeInfoSerializer, HomeSerializer
from django.shortcuts import render
from .models import HomeInfo

from rest_framework import generics


class HomeInfoList(generics.ListCreateAPIView):
    queryset = HomeInfo.objects.all()
    serializer_class = HomeSerializer


class HomeInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomeInfo.objects.all()
    serializer_class = HomeSerializer


def homeinfo(request):
    if request.method == 'POST':
        home = HomeInfo.objects.all()
        return render(request, 'homeinfo.html', {'data': home, 'sent': True})
    return render(request, 'homeinfo.html', content_type=None)