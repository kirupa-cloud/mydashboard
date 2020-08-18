from django.http import HttpResponse, JsonResponse
# from requests import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response

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




@api_view(['GET'])
def homedata(request):
    if request.method == 'GET':
        member=request.GET.get('membername')
        home = HomeInfo.objects.all()
        # (memberName__startswith=member)
        print(home)
        output = []
        for data in home:
            output.append(
                {'membername': data.memberName,
                 'dob': data.dob}
            )

        return JsonResponse(output, safe=False)


@api_view(['GET'])
def home_data(request):
    if request.method == 'GET':
        home = HomeInfo.objects.all()
        serializer = HomeSerializer(home, many=True)
        return Response(serializer.data)
        #
        # output = []
        # for data in home:
        #     output.append(
        #         {'membername': data.memberName,
        #          'dob': data.dob}
        #     )
        #
        # return JsonResponse(output, safe=False)
