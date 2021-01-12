from rest_framework import serializers
from .models import UtilityInfo, UtilityPayments, GroceryInfo


class UtiliyInfoSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="homeutils:utilityinfo-detail")

    class Meta:
        model = UtilityInfo
        fields = ['id', 'url', 'name', 'service_company', 'start_date', 'end_date']

        extra_kwargs = {"url":{"view_name":"utilityinfo-detail"}}

class UtiliyInfoSerializer2(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="homeutils:utilityinfo-detail")

    class Meta:
        model = UtilityInfo
        fields = ['id', 'url', 'name', 'start_date', 'end_date']

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


class UtilityPaymentSerializer2(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="utilitypayments-detail")
    utility = serializers.HyperlinkedRelatedField(view_name="UtilityPayment", read_only=True)

    class Meta:
        model = UtilityPayments
        fields = ['id',
                  'utility',
                  'url',
                  'status',
                  'service_start_date',
                  'amount'
                  ]



class GrocerySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GroceryInfo
        fields = '__all__'


class Detail(serializers.Serializer):
    name = serializers.ReadOnlyField()
    info = serializers.ReadOnlyField()
    comment = serializers.ReadOnlyField()

    def create(self, validated_data):
        pass
    def update(self, instance, validated_data):
        pass

