from rest_framework import serializers
from .models import UtilityInfo, UtilityPayments


class UtiliyInfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UtilityInfo
        fields = ['id', 'name', 'service_company', 'start_date', 'end_date']


class UtilityPaymentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UtilityPayments
        fields = ['id', 'utility_id', 'status', 'service_start_date', 'service_end_date', 'amount']

