from rest_framework import serializers
from .models import UtilityInfo


class UtiliyInfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UtilityInfo
        fields = ['id', 'name', 'service_company', 'start_date', 'end_date']

