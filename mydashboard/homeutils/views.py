from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response

from rest_framework import generics
from rest_framework import viewsets
from .serializers import *
from .models import *



class UtilityInfoView(generics.ListCreateAPIView):
    queryset = UtilityInfo.objects.all()
    serializer_class = UtiliyInfoSerializer


class UtilityDetails(generics.RetrieveUpdateAPIView):
    queryset = UtilityInfo.objects.all()
    serializer_class = UtiliyInfoSerializer


class UtilityNew(viewsets.ViewSet):

    def list(self, request):
        queryset = UtilityInfo.objects.all()
        serializers = UtiliyInfoSerializer(queryset, many=True)
        return Response(serializers.data)

    def retrieve(self, request, pk=None):
        queryset = UtilityInfo.objects.all()
        utility = get_object_or_404(queryset, pk=pk)
        serializers  = UtiliyInfoSerializer(utility)
        return Response(serializers.data)

