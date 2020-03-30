from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class Ping(APIView):
    permission_classes = [
        AllowAny
    ]

    def get(self, *args, **kwargs):
        output = dict(status=200)
        return Response(data=output)