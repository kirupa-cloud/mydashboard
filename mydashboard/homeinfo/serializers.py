from rest_framework import serializers
from homeinfo.models import HomeInfo


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeInfo
        fields = ['id', 'memberName', 'dob']



class HomeInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    memberName = serializers.CharField(required=True, allow_blank=False, max_length=100)
    dob = serializers.DateField()

    def create(self, validated_data):
        return HomeInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.memberName = validated_data.get('memberName', instance.memberName)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.save()
        return instance


