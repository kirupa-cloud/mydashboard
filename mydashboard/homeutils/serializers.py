from rest_framework import serializers
from .models import UtilityInfo, UtilityPayments


class UtiliyInfoSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="homeutils:utilityinfo-detail")

    class Meta:
        model = UtilityInfo
        fields = ['id', 'url', 'name', 'service_company', 'start_date', 'end_date']

        extra_kwargs = {"url":{"view_name":"utilityinfo-detail"}}

class UtilityPaymentSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="utilitypayments-detail")
    utility = serializers.HyperlinkedRelatedField(view_name="UtilityPayment", read_only=True)

    class Meta:
        model = UtilityPayments
        fields = ['id',
                  'utility',
                  'url',
                  'status',
                  'service_start_date',
                  'service_end_date',
                  'amount'
                  ]
